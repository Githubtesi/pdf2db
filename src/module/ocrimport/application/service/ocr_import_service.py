import os
import unicodedata
import pytesseract
from pdf2image import convert_from_path
from src.module.ocrimport.domain.model.ocr_text import OcrText
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List
import logging

logger = logging.getLogger(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPLER_PATH = r"C:\poppler-23.11.0\Library\bin"

class OcrImportService:
    def __init__(self, repository, max_workers: int = 8) -> None:
        self.repository = repository
        self.max_workers = max_workers

    def import_folder(self, folder_path: str) -> None:
        logger.info(f"OCR開始: folder_path={folder_path}")
        pdf_files = [
            os.path.join(root, file)
            for root, _, files in os.walk(folder_path)
            for file in files if file.lower().endswith(".pdf")
        ]
        logger.info(f"検出PDF件数: {len(pdf_files)}")

        # 並列実行
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_path = {
                executor.submit(self._ocr_pdf, path): path for path in pdf_files
            }
            for future in as_completed(future_to_path):
                path = future_to_path[future]
                content = future.result()
                ocr_text = OcrText(os.path.basename(path), content)
                self.repository.save(ocr_text)
                logger.info(f"OCR & DB保存完了: {path}")

    def _ocr_pdf(self, pdf_path: str) -> str:
        text = ""
        try:
            images = convert_from_path(pdf_path, poppler_path=POPLER_PATH)
            for image in images:
                page_text = pytesseract.image_to_string(
                    image, lang="eng+jpn", config="--psm 6"
                )
                text += page_text
            # 正規化+空白除去
            clean_text = unicodedata.normalize("NFKC", text)
            clean_text = clean_text.replace(" ", "").replace("　", "").replace("\n", "")
            logger.debug(f"OCR結果取得: {pdf_path} len={len(clean_text)}")
            return clean_text
        except Exception as e:
            logger.error(f"OCR失敗: {pdf_path} 理由: {e}")
            return ""

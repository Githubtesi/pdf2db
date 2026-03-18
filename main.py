import os
import time
from src.module.common.logger_config import setup_logging
from src.module.ocrimport.application.service.ocr_import_service import OcrImportService
from src.module.ocrimport.infrastructure.datasource.sqlite_ocr_text_repository import SqliteOcrTextRepository
import tkinter as tk
from tkinter import filedialog
import logging

logger = logging.getLogger(__name__)

def select_folder() -> str:
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        logger.warning("フォルダ未選択のため終了")
        exit(0)
    logger.info(f"選択フォルダ: {folder_selected}")
    return folder_selected

if __name__ == "__main__":
    setup_logging()
    folder = select_folder()
    repository = SqliteOcrTextRepository()
    service = OcrImportService(repository, max_workers=8)

    start_time = time.time()
    service.import_folder(folder)
    elapsed = time.time() - start_time

    logger.info(f"全OCR処理完了: 経過時間 = {elapsed/3600:.2f} 時間")

    # 60秒後にシャットダウン
    logger.info("PCを60秒後にシャットダウンします。中断したい場合は 'shutdown /a' をコマンドプロンプトで実行してください。")
    os.system("shutdown /s /t 60")


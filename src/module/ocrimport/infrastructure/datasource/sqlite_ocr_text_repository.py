from src.module.ocrimport.domain.repository.ocr_text_repository import OcrTextRepository
from src.module.ocrimport.domain.model.ocr_text import OcrText
import sqlite3
import logging

logger = logging.getLogger(__name__)

class SqliteOcrTextRepository(OcrTextRepository):
    def __init__(self, db_path: str = "ocr_texts.db") -> None:
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS texts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pdf_name TEXT,
                    content TEXT
                )
            ''')
        logger.debug(f"SQLiteテーブル初期化完了: db_path={self.db_path}")

    def save(self, ocr_text: OcrText) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO texts (pdf_name, content) VALUES (?, ?)",
                (ocr_text.pdf_name, ocr_text.content)
            )
        logger.debug(f"DB保存完了: {ocr_text.pdf_name}")

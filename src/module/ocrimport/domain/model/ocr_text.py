from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class OcrText:
    pdf_name: str
    content: str

    def __post_init__(self):
        if not self.pdf_name:
            logger.error(f"OcrText生成失敗: pdf_nameが空 {self=}")
            raise ValueError("pdf_nameは必須")
        # contentは空文字許容

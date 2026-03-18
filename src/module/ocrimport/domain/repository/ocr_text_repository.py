from abc import ABC, abstractmethod

class OcrTextRepository(ABC):
    @abstractmethod
    def save(self, ocr_texts):
        pass

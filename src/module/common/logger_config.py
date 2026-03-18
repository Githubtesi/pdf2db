# src/module/common/logger_config.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.FileHandler("process.log"),
            logging.StreamHandler()
        ]
    )

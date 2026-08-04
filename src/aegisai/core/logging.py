import logging
from pathlib import Path

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "aegisai.log"


def setup_logging() -> None:
    LOG_DIR.mkdir(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

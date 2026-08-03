import logging

from aegisai.core.logging import setup_logging


def main() -> None:
    setup_logging()

    logger = logging.getLogger(__name__)

    logger.info("AegisAI Bot is starting...")


if __name__ == "__main__":
    main()

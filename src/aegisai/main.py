import logging

from aegisai.bot.application import create_application
from aegisai.core.logging import setup_logging


def main() -> None:
    setup_logging()

    logger = logging.getLogger(__name__)

    logger.info("AegisAI Bot is starting...")

    application = create_application()

    logger.info(
        "Telegram application created: %s",
        application,
    )

    logger.info("Starting Telegram polling...")

    application.run_polling()


if __name__ == "__main__":
    main()

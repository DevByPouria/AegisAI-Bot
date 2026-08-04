from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from aegisai.handlers.help import help_command
from aegisai.handlers.message import message_handler
from aegisai.handlers.start import start_command


def register_handlers(application: Application) -> None:
    """Register all Telegram handlers."""

    application.add_handler(
        CommandHandler("start", start_command)
    )

    application.add_handler(
        CommandHandler("help", help_command)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )

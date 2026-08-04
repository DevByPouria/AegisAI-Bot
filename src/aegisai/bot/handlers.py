from telegram.ext import Application, CommandHandler

from aegisai.handlers.start import start_command


def register_handlers(application: Application) -> None:
    """Register all Telegram command handlers."""

    application.add_handler(
        CommandHandler("start", start_command)
    )

from telegram.ext import Application, CommandHandler

from aegisai.config.settings import settings
from aegisai.handlers.start import start_command


def create_application() -> Application:
    application = (
        Application.builder()
        .token(settings.bot_token)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start_command)
    )

    return application

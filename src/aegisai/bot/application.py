from telegram.ext import Application

from aegisai.bot.handlers import register_handlers
from aegisai.config.settings import settings


def create_application() -> Application:
    application = (
        Application.builder()
        .token(settings.bot_token)
        .build()
    )

    register_handlers(application)

    return application

from telegram.ext import Application

from aegisai.config.settings import settings


def create_application() -> Application:
    application = Application.builder().token(
        settings.bot_token
    ).build()

    return application

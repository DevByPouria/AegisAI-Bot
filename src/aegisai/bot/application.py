from telegram.ext import Application

from aegisai.bot.handlers import register_handlers
from aegisai.config.settings import settings
from aegisai.core.error import error_handler


def create_application() -> Application:
    application = Application.builder().token(settings.bot_token).build()

    application.add_error_handler(error_handler)

    register_handlers(application)

    return application

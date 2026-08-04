from telegram import Update
from telegram.ext import ContextTypes

from aegisai.services.greeting import build_welcome_message


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    message = build_welcome_message()

    await update.message.reply_text(message)

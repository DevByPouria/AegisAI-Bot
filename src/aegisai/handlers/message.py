from telegram import Update
from telegram.ext import ContextTypes

from aegisai.services.chat import build_chat_response


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None:
        return

    user_message = update.message.text

    if user_message is None:
        return

    response = build_chat_response(user_message)

    await update.message.reply_text(response)

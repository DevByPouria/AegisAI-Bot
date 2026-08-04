from telegram import Update
from telegram.ext import ContextTypes


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Handle regular text messages."""

    if update.message is None:
        return

    await update.message.reply_text(
        "فعلاً فقط دستورات را می‌شناسم 😊\n"
        "برای مشاهده آن‌ها از /help استفاده کن."
    )

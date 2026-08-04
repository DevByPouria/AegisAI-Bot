from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Show available commands."""

    await update.message.reply_text(
        
            "📚 Available Commands\n\n"
            "/start - Start the bot\n"
            "/help - Show this message"
        
    )

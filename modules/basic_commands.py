from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when the /start command is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! 👋\n\n"
        f"I am CrossAutomator Bot. I'm here to help you automate tasks across Telegram.\n"
        f"Use /help to see what I can do."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when the /help command is issued."""
    help_text = (
        "Here are my commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/about - Learn more about me\n"
        "/automate - Trigger a sample automation (placeholder)"
    )
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send an about message."""
    await update.message.reply_text(
        "🤖 CrossAutomator Bot\n\n"
        "A powerful automation bot built with the python-telegram-bot library.\n"
        "Designed for easy deployment on Railway.\n\n"
        "You can extend my features by adding new modules!"
    )

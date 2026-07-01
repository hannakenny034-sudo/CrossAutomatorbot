import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables.")

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message when /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hello {user.first_name}! 👋\n\n"
        f"I am CrossAutomator Bot. I'm here to help you automate tasks across Telegram.\n"
        f"Use /help to see what I can do."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message when /help is issued."""
    help_text = (
        "Here are my commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/about - Learn more about me\n"
        "/automate - Trigger a sample automation"
    )
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send an about message."""
    await update.message.reply_text(
        "🤖 CrossAutomator Bot\n\n"
        "A powerful automation bot built with python-telegram-bot.\n"
        "Designed for easy deployment on Railway.\n\n"
        "You can add more features by editing this file!"
    )

async def automate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Placeholder for automation commands."""
    await update.message.reply_text(
        "🔄 Automation feature is being set up!\n"
        "This is a placeholder command. You can replace me with your own logic."
    )

# Main function
def main():
    """Start the bot."""
    print("🤖 CrossAutomator Bot is starting...")
    
    # Create the Application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("automate", automate_command))

    # Start the bot
    print("✅ Bot is running and polling for updates...")
    application.run_polling()

if __name__ == '__main__':
    main()

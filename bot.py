import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from config import Config
from modules.basic_commands import start_command, help_command, about_command
from modules.automator import automate_command

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=Config.LOG_LEVEL
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    logger.info("Starting CrossAutomator Bot...")
    
    # Create the Application
    application = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))
    application.add_handler(CommandHandler("automate", automate_command))

    # Start the bot
    logger.info("Bot is running and polling for updates...")
    application.run_polling()

if __name__ == '__main__':
    main()

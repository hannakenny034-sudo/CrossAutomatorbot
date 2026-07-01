import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from config import Config
from modules import basic_commands, automator

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

    # Register command handlers from modules
    application.add_handler(CommandHandler("start", basic_commands.start_command))
    application.add_handler(CommandHandler("help", basic_commands.help_command))
    application.add_handler(CommandHandler("about", basic_commands.about_command))
    
    # Add your custom automation commands here
    # For example, a placeholder for an automator command
    application.add_handler(CommandHandler("automate", automator.automate_command))

    # Start the bot
    logger.info("Bot is running and polling for updates...")
    application.run_polling()

if __name__ == '__main__':
    main()

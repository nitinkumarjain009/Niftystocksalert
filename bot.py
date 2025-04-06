import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
import pytz
from datetime import datetime

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# --- Telegram Bot Configuration ---
# Replace with your actual Telegram Bot Token (get it from BotFather)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    print("Error: TELEGRAM_BOT_TOKEN environment variable not set!")
    exit()

# Replace with the Chat ID where you want the bot to send messages
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
if not CHAT_ID:
    print("Error: TELEGRAM_CHAT_ID environment variable not set!")
    exit()

# --- Time Zone Configuration ---
INDIA_TIMEZONE = pytz.timezone('Asia/Kolkata')

# --- Scheduler ---
scheduler = BackgroundScheduler()

# --- Bot Command Handlers ---
def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message when the /start command is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}! I am your financial bot\.',
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Sends a help message when the /help command is issued."""
    update.message.reply_text('Use /start to begin. More commands will be added later.')

# --- Scheduled Tasks ---
def scheduled_task(context: CallbackContext) -> None:
    """Example of a scheduled task."""
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    now_india = now_utc.astimezone(INDIA_TIMEZONE)
    message = f"This is a scheduled message at {now_india.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    context.bot.send_message(chat_id=CHAT_ID, text=message)
    logger.info(f"Sent scheduled message: {message}")

def main() -> None:
    """Starts the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start the scheduler
    scheduler.start()

    # Schedule the example task to run every minute (for testing)
    scheduler.add_job(scheduled_task, 'interval', minutes=1, id='example_task')

    # Start the Bot
    updater.start_polling()

    # Keep the bot running until you press Ctrl-C
    updater.idle()

    # Shut down the scheduler cleanly
    scheduler.shutdown()

if __name__ == '__main__':
    main()

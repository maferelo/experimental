"""
Simple Bot to send timed Telegram messages.

This Bot uses the Application class to handle the bot and the JobQueue to send
timed messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.

Note:
To use the JobQueue, you must install PTB via
`pip install "python-telegram-bot[job-queue]"`
"""

import feedparser
import pickle
import logging
import time

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

CHAT_ID = "713301950"
FEEDS = (
    "https://www.nature.com/nmat.rss",
    "https://dynomight.net/feed.xml",
    "https://www.sciencedaily.com/rss/top/science.xml",
    "https://www.science.org/rss/news_current.xml",
    "https://www.newscientist.com/section/news/feed/",
    "https://phys.org/rss-feed/",
    "https://www.wipo.int/patentscope/en/rss.xml"
    "https://www.understandingwar.org/feeds.xml",
    "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines"
)
TOKEN = ""
POLL_FEED_INTERVAL = 60  # 60 seconds 

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

def get_new_rss_entries():
    all_entries = []
    for feed in FEEDS:
        all_entries.extend(feedparser.parse(feed).entries)
    current_entries = {entry["link"] for entry in all_entries}

    try:
        with open("rss_last_entries", 'rb') as f:
            last_entries = pickle.load(f)
    except FileNotFoundError:
        last_entries = set()
    
    if current_entries - last_entries:
        with open("rss_last_entries", 'wb') as f:
            pickle.dump(current_entries, f)

    return current_entries - last_entries

async def message_new_rss_entries(bot, chat_id):
    last_entries = get_new_rss_entries()
    if last_entries:
        for entrie in last_entries:
            await bot.send_message(chat_id, text=f"{entrie}")


# Define a few command handlers. These usually take the two arguments update and
# context.
# Best practice would be to replace context with an underscore,
# since context is an unused local variable.
# This being an example and not having context present confusing beginners,
# we decided to have it present as context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Hi! Use /set <seconds> to set a timer")


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the alarm message."""
    await message_new_rss_entries(context.bot, context.job.chat_id)


def remove_job_if_exists(name: str, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add a job to the queue."""
    chat_id = update.effective_message.chat_id
    try:
        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_repeating(alarm, POLL_FEED_INTERVAL, chat_id=chat_id, name=str(chat_id), data=POLL_FEED_INTERVAL)

        text = "Timer successfully set!"
        if job_removed:
            text += " Old one was removed."
        await update.effective_message.reply_text(text)

    except (IndexError, ValueError):
        await update.effective_message.reply_text("Usage: /set <seconds>")


async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Remove the job if the user changed their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Timer successfully cancelled!" if job_removed else "You have no active timer."
    await update.message.reply_text(text)


async def send_start_message(self):
    self.job_queue.run_repeating(alarm, POLL_FEED_INTERVAL, chat_id=CHAT_ID, name=CHAT_ID, data=POLL_FEED_INTERVAL)


def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("set", set_timer))
    application.add_handler(CommandHandler("unset", unset))

    application.post_init = send_start_message

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
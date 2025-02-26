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

import io
import logging
import os
import time

import feedparser
import pickle
import requests

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from bot import run as scrape_run
from analyse import main as run_analyse

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data


load_dotenv()  # take environment variables from .env.

CHAT_ID = "713301950"

def get_feeds():
    return [
        # Science
        "https://www.nature.com/nmat.rss",
        "https://dynomight.net/feed.xml",
        "https://www.sciencedaily.com/rss/top/science.xml",
        "https://www.science.org/rss/news_current.xml",
        "https://www.newscientist.com/section/news/feed/",
        "https://phys.org/rss-feed/",
        "https://www.wipo.int/patentscope/en/rss.xml"
        "https://www.understandingwar.org/feeds.xml",
        "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines",
        
        # Tech
        "https://news.mit.edu/rss/research",
        "https://www.uber.com/blog/engineering/rss/",
        "https://engineering.atspotify.com/feed/",
        "https://slack.engineering/feed",
        "http://www.forbes.com/entrepreneurs/index.xml",
        "http://venturebeat.com/feed/"
        
        # Stocks
        "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines",
        "https://feeds.content.dowjones.io/public/rss/mw_marketpulse",
        
        # E-commerce
        "https://trends.google.com/trending/rss?geo=US",
        "https://www.trendhunter.com/rss",
        "https://www.theverge.com/rss/index.xml",
        "https://www.trustedreviews.com/feed",
        "http://feeds.slashgear.com/slashgear",
        "https://www.engadget.com/rss.xml",
    ]



FEEDS = get_feeds()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
POLL_FEED_INTERVAL = 30  # 60 seconds 

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

def get_new_rss_entries():
    all_entries = []
    for feed in FEEDS:
        try:
            response = requests.get(feed, timeout=5)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching feed {feed}: {e}")
            continue
        except requests.exceptions.Timeout as e:
            logging.error(f"Timeout fetching feed {feed}: {e}")
            continue
        content = io.BytesIO(response.content)
        all_entries.extend(feedparser.parse(content).entries)
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
            time.sleep(7)
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
    
# Define the prepare_data function
def prepare_data(data, n_steps):
    x, y = [], []
    for i in range(len(data) - n_steps):
        x.append(data[i:(i + n_steps), 0])
        y.append(data[i + n_steps, 0])
    return np.array(x), np.array(y)

def create_lstm_model(input_shape):
    """
    Create and compile an LSTM model for time series prediction.

    Parameters:
    - input_shape (tuple): Shape of the input data in the form (time_steps, features).

    Returns:
    - model (Sequential): Compiled LSTM model.
    """
    model = Sequential()
    # Add the first LSTM layer with 50 units and return sequences for the next layer
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    # Add the second LSTM layer with 50 units
    model.add(LSTM(units=50))
    # Add a Dense layer with 1 unit for regression
    model.add(Dense(units=1))
    
    # Compile the model using the Adam optimizer and Mean Squared Error loss
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    return model
    
def predict_stock_price():
    stock_symbol = 'AAPL'
    stock_data = yf.download(stock_symbol,  period="max")
    closing_prices = stock_data['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    closing_prices_scaled = scaler.fit_transform(closing_prices)
    # Code snippet for creating and training the LSTM model
    n_steps = 60

    # Prepare the training data using the defined function
    x_train, y_train = prepare_data(closing_prices_scaled, n_steps)

    # Reshape the input data to fit the LSTM model
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # Create an instance of the LSTM model
    model = create_lstm_model((x_train.shape[1], 1))

    # Train the model on the training data
    model.fit(x_train, y_train, epochs=3, batch_size=32)
    
    # Code snippet for making predictions and evaluation
    train_predictions = model.predict(x_train)
    train_predictions = scaler.inverse_transform(train_predictions)
    mse = mean_squared_error(closing_prices[n_steps:], train_predictions)
    
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index[n_steps:], closing_prices[n_steps:], label='Actual Prices', color='blue')
    plt.plot(stock_data.index[n_steps:], train_predictions, label='Predicted Prices', color='red')
    plt.title(f'{stock_symbol} Stock Price Prediction using LSTM')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.savefig('predict.png')
        
    return f'Mean Squared Error on Training Data: {mse}'


async def alarm(context: ContextTypes.DEFAULT_TYPE) -> None:
    await message_new_rss_entries(context.bot, context.job.chat_id)

async def scrape_aliexpress(context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(context.job.chat_id, "Scraping...")
    result = await scrape_run()
    await context.bot.send_message(context.job.chat_id, text=f"Found {result} products")

async def analyse_aliexpress(context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(context.job.chat_id, "analyse_aliexpress...")
    result = await run_analyse()
    await context.bot.send_message(context.job.chat_id, text=f"Best Ali products: {result}")

    
async def predict(context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(context.job.chat_id, "Predicting...")
    await context.bot.send_message(context.job.chat_id, predict_stock_price())
    await context.bot.send_photo(context.job.chat_id, photo=open('predict.png', 'rb'))
    
async def boot(context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(context.job.chat_id, "Booting...")

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


async def post_init(self):
    self.job_queue.run_once(boot, 0, chat_id=CHAT_ID)

    self.job_queue.run_repeating(alarm, POLL_FEED_INTERVAL, chat_id=CHAT_ID, name=CHAT_ID, data=POLL_FEED_INTERVAL)
    self.job_queue.run_repeating(predict, 60, first=60, chat_id=CHAT_ID)
    self.job_queue.run_repeating(scrape_aliexpress, 60 * 12, first=60, chat_id=CHAT_ID)
    self.job_queue.run_repeating(analyse_aliexpress, 60 * 12, first=60 * 6, chat_id=CHAT_ID)


def main() -> None:
    """Run bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("set", set_timer))
    application.add_handler(CommandHandler("unset", unset))

    application.post_init = post_init

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    

import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

async def yourname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Volodymyr")

async def howoldareyou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am 24 years old")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    start_handler = CommandHandler('hello', hello)
    start_handler = CommandHandler('yourname', yourname)
    start_handler = CommandHandler('howoldareyou', howoldareyou)
    application.add_handler(start_handler)

    application.run_polling()
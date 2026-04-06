import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

SERVER_URL = os.getenv("SERVER_URL")
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    r = requests.post(SERVER_URL, json={"message": user_msg})
    reply = r.json().get("reply", "No reply")
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()

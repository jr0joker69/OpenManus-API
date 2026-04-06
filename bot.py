from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests, os

TOKEN = os.getenv("TELEGRAM_TOKEN")
SERVER_URL = os.getenv("SERVER_URL", "https://your-render-service.onrender.com/chat")

async def start(update, context):
    await update.message.reply_text("Hello! Send me a message and I'll forward it to OpenClaude.")

async def handle_message(update, context):
    user_text = update.message.text
    resp = requests.post(SERVER_URL, json={"message": user_text}).json()
    await update.message.reply_text(resp["reply"])

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()

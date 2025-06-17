# interfaces/telegram_bot/bot_core.py

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from sigma_avatarus import SigmaAvatarus
from fdl_agent_kernel.logic_core import FDLKernel
from fdl_codeagents.api_wrapper import FDLCodeAgent

# Placeholder: вставьте свой API-ключ OpenAI и Telegram
OPENAI_KEY = "your-openai-key"
TELEGRAM_TOKEN = "your-telegram-token"

avatar = SigmaAvatarus()
kernel = FDLKernel()
agent = FDLCodeAgent(api_key=OPENAI_KEY, kernel=kernel)

# Запуск логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Я GPT-агент резонансной логики НОВЕЯ. Задай вопрос.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    semantic_response = avatar.resonate(user_input)
    ai_response = agent.query(prompt=user_input, context=semantic_response)
    await update.message.reply_text(ai_response)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Telegram GPT Agent запущен.")
    app.run_polling()

if __name__ == "__main__":
    main()

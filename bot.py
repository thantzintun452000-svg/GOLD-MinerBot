from telegram.ext import Application, CommandHandler

# /start command
async def start(update, context):
    await update.message.reply_text("Hello! Bot is running on GitHub Actions 🚀")

def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # မင်းရဲ့ BotFather Token ထည့်ရန်

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()

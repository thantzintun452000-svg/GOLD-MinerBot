from telegram.ext import Application, CommandHandler

# /start command
async def start(update, context):
    await update.message.reply_text("Hello 👋 Bot အလုပ်လုပ်နေပါပြီ!")

def main():
    TOKEN = "8261763462:AAFLl4RTMctrrLMU4_0kPJ2vkdUuwVXd7gA"  # မင်းရဲ့ အသစ် Bot Token

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()

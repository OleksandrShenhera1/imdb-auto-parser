from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegramParser import parser
from telegramBotLogic import *
TOKEN: Final = 'your token'

BOT_USERNAME: Final = 'your name'


startMessage = ("your info")

helpMessage = ("your info")
# Start & help
async def startCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(startMessage)


async def helpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(helpMessage)

# Error command

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused error {context.error}")


# Custom commands   


async def topCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top = getTop()
    chunk = ""
    for line in top:
        if len(chunk) + len(top) + 1 > 4096:
            await update.message.reply_text(chunk.strip(), parse_mode="HTML", disable_web_page_preview=True)
            chunk = ""
        chunk += line + "\n"
    if chunk:
        await update.message.reply_text(chunk.strip(), parse_mode="HTML", disable_web_page_preview=True)


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    # Main commands

    # Your handlers for BotFather Commands!!!
    app.add_handler(CommandHandler('start', startCommand))
    app.add_handler(CommandHandler('help', helpCommand))
    app.add_handler(CommandHandler('top', topCommand))
    # Error command
    app.add_error_handler(error)
    # polling time
    app.run_polling(poll_interval=2)

    print(f"Bot is running...")
from email.policy import default
import imp
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler,filters
from utils import validate,sensorReading

username=""
password=""
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg="Fire Alert Bot \n/register - To register your device\n/status - To check status of your device\n/remove to Remove your device"
    print(update.effective_chat)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)



async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg=""
    if(len(context.args)==0):
        msg="Invalid format\nType in given format\n\n/register username password"
    else:
        username=context.args[0]
        password=context.args[1]
        msg=validate(username,password,update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    readings=sensorReading(update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=readings)



    

if __name__ == '__main__':
    TOKEN = "TELEGRAM TOKEN"
    application = ApplicationBuilder().token(TOKEN).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    register_handler = CommandHandler('register', register)
    status_handler = CommandHandler('status', status)

    application.add_handler(start_handler)
    application.add_handler(status_handler)
    application.add_handler(register_handler)
    application.add_handler(echo_handler)
    

    application.run_polling()

    application.run_polling()



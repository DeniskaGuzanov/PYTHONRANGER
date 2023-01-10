
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater("5949291118:AAGgBDmVrDRykrHsakY9qMT8fIzzT33VNsk")
updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('server start')
updater.start_polling()

updater.idle()
from telebot import TeleBot, types
 
TOKEN = '55977171043:AAEuRUXIfOolC1mnHjdfv_xrPqlZ1Lx__hU'
 
bot = TeleBot(TOKEN)
 
 
@bot.message_handler()
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text)
 
 
bot.polling()
import exportFile, addContact, deletContact, viewContact
from addContact import add, create
from bot import TOKEN
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)
import logging
import controller

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

MENU = range(1)

def start(update, _):
    update.message.reply_text(f'Привет,{update.effective_user.first_name}, это твоя телефонная книга. Выбери команду\n')
    update.message.reply_text('1 - Создать новый справочник; \n 2. Добавить новый контакт;\n 3. Экспортировать контакты в файл; \n'
    '4. Удалить контакт; \n 5. Показать все контакты')
    return MENU



def menu(update, context):
    user = update.message.from_user
    logger.info('Выбор операции: %s: %s', user.first_name, update.message.text)
    user_menu = update.message.text
    if user_menu in '1234':
        if user_menu == '1':
            update.message.reply_text('Создать новый справочник')
            return create
        if user_menu == '2':
            update.message.reply_text('Добавить новый контакт')
            return add
        if user_menu == '3':
            update.message.reply_text('Экспортировать контакты в файл')
            return exportFile
        if user_menu == '4':
            update.message.reply_text('Удалить контакт')
            return deletContact
        if user_menu == '5':
            update.message.reply_text('Показать все контакты')
            return viewContact
    # else:
    #     update.message.reply_text('Ошибка ввода')
    #     return ConversationHandler.END
    #     # return check.number_check()



def cancel(update, _):
    user = update.message.from_user
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    

    conversation_handler = ConversationHandler(  
    
        entry_points=[CommandHandler('start', start)],
    
        states={
        
            MENU: [MessageHandler(Filters.text, menu)]
           
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    
        
    )

    dispatcher.add_handler(conversation_handler)
    print('server start')
    updater.start_polling()
    updater.idle()
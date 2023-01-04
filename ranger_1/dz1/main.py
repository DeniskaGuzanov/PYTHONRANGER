import logging
from bot import TOKEN
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)

# Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CHOICE, NUMBER_ONE, NUMBER_TWO, NUMBER_OPERATION= range(4)

def start(update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, это - калькулятор. Выберите пожалуйста команду.\n' 'Команда /cancel, чтобы прекратить разговор.\n\n')
    update.message.reply_text('1 - операции с числами; \n2 - Выйти из калькулятора \n')
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '12':
        if user_choice == '1':
            update.message.reply_text('Введите первое число:\n ')
            return NUMBER_ONE
        if user_choice == '2':
            update.message.reply_text('Спасибо, до свидания!')
            return ConversationHandler.END     
    else:
        update.message.reply_text('Ошибка ввода. Введите цифру операции: \n 1 - операции с числами;\n3 - для выхода \n')

def number_one(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_one'] = get_number
        update.message.reply_text('Введите второе число')
        return NUMBER_TWO

    else:
        update.message.reply_text('Нужно ввести число')


def number_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_two'] = get_number
        update.message.reply_text('Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')
        return NUMBER_OPERATION


def number_operation(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    number_one = context.user_data.get('number_one')
    number_two = context.user_data.get('number_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = number_one + number_two
        if user_choice == '-':
            result = number_one - number_two
        if user_choice == '*':
            result = number_one * number_two
        if user_choice == '/':
            try:
                result = number_one / number_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Результат: {number_one} {user_choice} {number_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n' )


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(  
    
        entry_points=[CommandHandler('start', start)],
    
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            NUMBER_ONE: [MessageHandler(Filters.text, number_one)],
            NUMBER_TWO: [MessageHandler(Filters.text, number_two)],
            NUMBER_OPERATION: [MessageHandler(Filters.text, number_operation)],
          
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    
        
    )

    dispatcher.add_handler(conversation_handler)
    print('server start')
    updater.start_polling()
    updater.idle()
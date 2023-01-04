import json
import controller
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def create():
    json_data = []
    with open('basa_d.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
        return controller.user_controller()


def add(update, context):
    name = update.message.from_user(input("Введите имя: "))
    logger.info("Пользователь ввел число: %s: %s", name.first_name, update.message.text)
    get_user = update.message.text
    context.user_data[add] = get_user
    update.message.reply_text(surname = input('Введите Фамилию'))
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    base_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data = json.load(open("basa_d.json"))
    data.append(base_data)
    with open("basa_d.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nКонтакт успешно добавлен\n')
    return controller.user_controller()
def add(bot, update):
    print('json file update : ' ,update)
    print('json file bot : ', bot)
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    print("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))
    bot.sendMessage(chat_id, 'text')
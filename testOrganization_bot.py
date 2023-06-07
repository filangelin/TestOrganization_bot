from telebot import TeleBot, types
from faker import Faker

bot = TeleBot(token='токен', parse_mode='html')

faker = Faker('ru_RU')


organization_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
organization_type_keybaord.row(
    types.KeyboardButton(text='ИНН'),
    types.KeyboardButton(text='ОГРН'),
)
organization_type_keybaord.row(
    types.KeyboardButton(text='КПП'),
    types.KeyboardButton(text='Адрес'),
)
organization_type_keybaord.row(
    types.KeyboardButton(text='email'),
    types.KeyboardButton(text='Сотрудник'),
)

@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.from_user.first_name + ', привет! Здесь ты сможешь сгенерировать тестовые данные для своей организации.\nВыбери, что тебе нужно☺️',
        reply_markup=organization_type_keybaord,
    )

@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'ИНН':
        text = "Тестовый ИНН"
        otvet = faker.businesses_inn()
    elif message.text == 'ОГРН':
        text = "Тестовый ОГРН"
        otvet = faker.businesses_ogrn()
    elif message.text == 'КПП':
        text = "Тестовый КПП"
        otvet = faker.kpp()
    elif message.text == 'Адрес':
        text = "Тестовый адрес"
        otvet = faker.address()
    elif message.text == 'email':
        text = "Тестовый email"
        otvet = faker.ascii_safe_email()
    elif message.text == 'Сотрудник':
        text = "Тестовый сотрудник"
        otvet = faker.name()

    else:
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return

    bot.send_message(
        chat_id=message.chat.id,
        text=f'{text} :\n<code>{otvet}</code>'
    )

def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()

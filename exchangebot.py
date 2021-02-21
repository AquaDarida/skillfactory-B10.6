import telebot
from extensions import VALUES, APIException, Exchange

with open("config.ini") as f:
    TOKEN = f.readline()[8:].replace("\n", "")
    print(TOKEN)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def info(message: telebot.types.Message):
    response = "Бот предназначен для конвертации валют. Чтобы увидеть какие валюты поддерживает бот, используйте " \
               "/values \nДля конвертации используйте следующий формат:\n<валюта, которую конвертировать> <валюта, " \
               "в которую конвертировать> <количество>\nПримеры использования:\nвона фунт 200\nдоллар лира 50\nрупия " \
               "рэнд 120"
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    response = 'Доступные валюты:'
    for key in VALUES.keys():
        response += f'\n{key}'
    bot.send_message(message.chat.id, response)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:

        values_ = message.text.lower().split(' ')
        if len(values_) != 3:
            raise APIException('Неверный формат. Примеры ввода можено посмотреть через /help')

    except APIException as ex:
        bot.reply_to(message, f'{ex}')
    except Exception:
        bot.reply_to(message, 'Произошла ошибка обработки команды')

    else:
        bot.reply_to(message, Exchange.get_price(*values_))


bot.polling()

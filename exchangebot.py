import telebot
from extensions import VALUES

with open("config.ini") as f:
    TOKEN = f.readline()[9:].replace("\n", "")
    print(TOKEN)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ""
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    values_ = ''
    for key in VALUES.keys():
        values_ += f'{key}\n'
    response = f'Доступные валюты:\n{values_}\n\
        (доллар = доллар США,\n\
        вона = южнокорейская вона,\n\
        фунт = британский фунт,\n\
        франк = швейцарский франк,\n\
        крона =чешская крона,\n\
        рупия = индийская рупия,\n\
        лира = турецкая лира,\n\
        рэнд = южноафриканский рэнд)'
    bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['examples'])
def examples(message: telebot.types.Message):
    response = ""
    bot.send_message(message.chat.id, response)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
   response = ""
   bot.send_message(message.chat.id, response)


bot.polling()
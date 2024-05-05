#TranBot                                                                        '''Бот для перевода текста'''

import telebot, deeptranslate as tran
token = input('insert your token... ')
print('starting...')

bot = telebot.TeleBot(token)                                            #Токен бота

print('the bot has started!')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, 'Привет! 👋 Я - TranBot. Я способен переводить текст с русского языка на английский или наоборот. Для начала работы введите фразу для перевода. ')

@bot.message_handler(content_types=['text'])                                    #Метод для получения текст. сообщений
def get_text_messages(message):
    bot.send_message(message.from_user.id, 'Загрузка... ⏳')
    bot.edit_message_text(tran.translateEn(message.text), message.from_user.id, message.id + 1)
    print('RuEN - ', message.text, ' -- ', tran.translateEn(message.text))

bot.infinity_polling(none_stop = True, interval = 0)
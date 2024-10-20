import telebot, deeptranslate as tran

token = input('insert token: ')
print('starting...')

bot = telebot.TeleBot(token)

print('the bot has started!')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id, 'Привет! 👋 Я - TranBot. Я способен переводить текст с русского языка на английский или испанский и наоборот. Для начала работы введите фразу для перевода. Укажите целевой язык (en или es), например: "en: Привет" или "es: Hola".')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text.strip()
    target_language = text.split(':')[0].strip()  # Retrieve the language code
    text_to_translate = ':'.join(text.split(':')[1:]).strip()  # Retrieve text to translate

    bot.send_message(message.from_user.id, 'Загрузка... ⏳')

    try:
        if target_language == 'en':
            translated_text = tran.translateEn(text_to_translate)
        elif target_language == 'es':
            translated_text = tran.translateEs(text_to_translate)
        else:
            bot.send_message(message.from_user.id, 'Неправильный язык. Используйте "en:" для английского и "es:" для испанского.')
            return
        
        bot.edit_message_text(translated_text, message.from_user.id, message.id + 1)
        print(f'Ru{target_language.upper()} - {text_to_translate} -- {translated_text}')
    except Exception as e:
        bot.send_message(message.from_user.id, 'Произошла ошибка при переводе. Попробуйте еще раз.')

bot.infinity_polling(none_stop=True, interval=0)
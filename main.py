import telebot, deeptranslate as tran, database

token = input('insert token: ')
print('starting...')

bot = telebot.TeleBot(token)  #получение токена для бота

print('the bot has started!')

def create_language_keyboard():
    #метод создания клавиатуры для выбора языка
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton("🇬🇧 Английский", callback_data="set_language_en"),
        telebot.types.InlineKeyboardButton("🇪🇸 Испанский", callback_data="set_language_es")
    )
    return keyboard


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.from_user.id,
                     "Привет! 👋 Я - TranBot. Я способен переводить текст с русского языка на английский или испанский и наоборот. Для начала работы введите фразу для перевода. Укажите целевой язык (en или es), например: \"en: Привет\" или \"es: Hola\".",
                     reply_markup = create_language_keyboard()) #вывод стартового сообщения и клавиатуры
    database.add_new_user(message.from_user.id, message.from_user.username) #добавление нового пользователя в БД (см database.py)


@bot.callback_query_handler(func=lambda call: call.data.startswith("set_language_")) #хэндлер команды выбора языка:
def handle_language_selection(call): #используется лямбда-функция для отсеивания колбэков и ответа только на выбор языка
    user_id = call.from_user.id
    selected_language = call.data.split("_")[-1]  # Получаем "en" или "es"

    # Сохраняем выбранный язык в базу данных
    database.set_user_language(user_id, selected_language)

    # Уведомляем пользователя
    bot.answer_callback_query(call.id, f"Язык изменён на {'Английский' if selected_language == 'en' else 'Испанский'}")
    bot.send_message(user_id, f"Выбранный язык: {'🇬🇧 Английский' if selected_language == 'en' else '🇪🇸 Испанский'}")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user_id = message.from_user.id
    text_to_translate = message.text.strip()

    # Получаем выбранный язык из базы данных
    target_language = database.get_user_language(user_id)[0]
    print(f'the language of user {user_id} is {target_language}')

    bot.send_message(user_id, 'Загрузка... ⏳')     #отправка процесс-сообщения

    try:
        # Перевод текста
        if target_language == 'en':
            translated_text = tran.translateEn(text_to_translate)
        elif target_language == 'es':
            translated_text = tran.translateEs(text_to_translate)
        else:
            bot.send_message(user_id,
                             'Неправильный язык. Используйте "en:" для английского и "es:" для испанского.')
            return

        bot.edit_message_text(translated_text, message.from_user.id, message.id + 1)
        print(f'Ru{target_language.upper()} - {text_to_translate} -- {translated_text}')    #вывод сообщения о переводе в консоль

    except Exception as e:
        bot.send_message(user_id, f'Произошла ошибка при переводе: {str(e)}')
        print(f'Error translating text: {str(e)}')


bot.infinity_polling(none_stop=True, interval=0)  #цикличная работа бота

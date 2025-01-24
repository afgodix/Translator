import sqlite3

connection = sqlite3.connect('trandb.db', check_same_thread=False)
cursor = connection.cursor()

def add_new_user(user_id, username):      #функция добавления нового пользователя
    cursor.execute('''
    INSERT OR IGNORE INTO Users (id, username, lastSelectedLanguage) VALUES (?, ?, ?)
    ''', (user_id, username, 'no'))
    connection.commit()
    print('start command executed')

def set_user_language(user_id, new_language):
    cursor.execute('''
    UPDATE Users SET lastSelectedLanguage = ? WHERE id = ?
    ''', (new_language, user_id))   #изменение языка пользователя
    connection.commit()
    print(f'language got changed for user {user_id} to {new_language}')

def get_user_language(user_id):
    cursor.execute('SELECT lastSelectedLanguage FROM Users WHERE id = ?', (user_id,))
    return cursor.fetchall()[0]      #получение языка пользователя в БД

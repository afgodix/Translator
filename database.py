import sqlite3

connection = sqlite3.connect('trandb.db')
cursor = connection.cursor()

def add_new_user(user_id, username):
    try:
        cursor.execute('''
        INSERT OR IGNORE INTO Users (id, username, lastSelectedLanguage) VALUES (?, ?, ?)
        ''', (user_id, username))
        print('new user inserted')
    except Exception:
        print('error occured')


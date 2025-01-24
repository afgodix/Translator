import sqlite3

connection = sqlite3.connect('trandb.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    lastSelectedLanguage VARCHAR(3) NOT NULL,
    UNIQUE(id)
    )
    '''
)

connection.commit()
print('success')
connection.close()
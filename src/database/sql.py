import sqlite3
# Ścieżka do pliku bazy danych w sqlite
DATABASE = 'database.db'

# Połączenie sie z bazą danych
conn = sqlite3.connect(DATABASE)
# Stworzenie tabeli w bazie danych za pomocą sqlite3
conn.execute('CREATE TABLE IF NOT EXISTS users (userId Integer PRIMARY KEY, email TEXT UNIQUE NOT NULL, username TEXT UNIQUE NOT NULL, password TEXT, isAdmin BOOLEAN)')
conn.execute('CREATE TABLE IF NOT EXISTS mapPointers (pointerId Integer PRIMARY KEY, long REAL NOT NULL, lan REAL NOT NULL, createdOn TEXT NOT NULL, userId INTEGER NOT NULL, FOREIGN KEY(userId) REFERENCES users(userId))')
cur = conn.cursor()
cur.execute("INSERT OR IGNORE INTO users (email,username,password,isAdmin) VALUES (?,?,?,?)",('test@email.com','Admin','123', True) )
conn.commit()
# Zakończenie połączenia z bazą danych
conn.close()
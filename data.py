import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, user_name TEXT, user_password TEXT)")
conn.commit()
sql = 'INSERT INTO users VALUES (NULL, ?, ?)'
c.execute(sql, ('roy', 'pass'))
conn.commit()
conn.close()
print('Database created successfully!')
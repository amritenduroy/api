import sqlite3
import pandas as pd

df = pd.read_csv('books.csv', encoding='utf8')
row = df.shape[0]

conn = sqlite3.connect('data.db')
c = conn.cursor()

# creating users table and populate with data
c.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, user_name TEXT, user_password TEXT)")
conn.commit()

sql = 'INSERT INTO users VALUES (NULL, ?, ?)'
c.execute(sql, ('roy', 'pass'))
conn.commit()

# creating books table and populate with data
sql = """ 
    CREATE TABLE books (
        bookID INT,
        title TEXT,
        authors TEXT,
        average_rating FLOAT,
        isbn TEXT,
        isbn13 TEXT,
        language_code TEXT,
        num_pages INT,
        ratings_count INT,
        text_reviews_count INT
    )
"""
c.execute(sql)
conn.commit()

sql = 'INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

data = df.itertuples(index=False, name=None)

for d in data:
    #print(d)
    c.execute(sql, d)
    conn.commit()
conn.close()
print('Database created successfully!')


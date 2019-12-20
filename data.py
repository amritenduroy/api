import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY, user_name TEXT, user_password TEXT)")
conn.commit()

sql = 'INSERT INTO users VALUES (NULL, ?, ?)'
c.execute(sql, ('roy', 'pass'))
conn.commit()

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

data = [
    (1,'Harry Potter and the Half-Blood Prince (Harry Potter  #6)','J.K. Rowling-Mary GrandPrÃ©',4.56,'439785960','9780439785969','eng',652,1944099,26249),
    (2,'Harry Potter and the Order of the Phoenix (Harry Potter  #5)','J.K. Rowling-Mary GrandPrÃ©',4.49,'439358078','9780439358071','eng',870,1996446,27613),
    (4,'Harry Potter and the Chamber of Secrets (Harry Potter  #2)','J.K. Rowling',4.41,'439554896','9780439554893','eng',352,6267,272),
    (5,'Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)','J.K. Rowling-Mary GrandPrÃ©',4.55,'043965548X','9780439655484','eng',435,2149872,33964),
    (8,'Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)','J.K. Rowling-Mary GrandPrÃ©',4.78,'439682584','9780439682589','eng',2690,38872,154),
    (9,'Unauthorized Harry Potter Book Seven News: "Half-Blood Prince" Analysis and Speculation','W. Frederick Zimmerman',3.69,'976540606','9780976540601','en-US',152,18,1),
    (10,'Harry Potter Collection (Harry Potter  #1-6)','J.K. Rowling',4.73,'439827604','9780439827607','eng',3342,27410,820)
]
for d in data:
    sql = 'INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    c.execute(sql, d)
    conn.commit()

conn.close()
print('Database created successfully!')


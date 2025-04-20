import sqlite3


conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Tbale Creation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price REAL
    )
''')

# Data Insertion
sales_data = [
    ('Product A', 10, 15.5),
    ('Product B', 5, 20.0),
    ('Product A', 7, 15.5),
    ('Product C', 3, 50.0),
    ('Product B', 2, 20.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)
conn.commit()
conn.close()

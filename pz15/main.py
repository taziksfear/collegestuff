import sqlite3

conn = sqlite3.connect('internet_shop.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer TEXT NOT NULL,
    item TEXT NOT NULL,
    unit TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    cost REAL NOT NULL
)
''')

sample_data = [
    ("Иванов", "Книга", "шт", 2, 500),
    ("Петров", "Молоко", "л", 1, 80),
    ("Сидоров", "Ноутбук", "шт", 1, 45000)
]

cursor.executemany('''
INSERT INTO sales (buyer, item, unit, quantity, cost)
VALUES (?, ?, ?, ?, ?)
''', sample_data)

conn.commit()

cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
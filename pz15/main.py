import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('internet_shop.db')
        print(f"Подключение к SQLite успешно, версия SQLite: {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Ошибка при подключении к SQLite: {e}")
    return conn

def create_table(conn):
    try:
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
        conn.commit()
        print("Таблица 'sales' создана или уже существует")
    except Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def insert_sample_data(conn):
    sample_data = [
        ("Иванов", "Книга", "шт", 2, 500),
        ("Петров", "Молоко", "л", 1, 80),
        ("Сидоров", "Ноутбук", "шт", 1, 45000),
        ("Кузнецов", "Телефон", "шт", 1, 30000),
        ("Васильев", "Кофе", "кг", 0.5, 600),
        ("Николаев", "Чай", "кг", 0.3, 400),
        ("Алексеев", "Принтер", "шт", 1, 15000),
        ("Дмитриев", "Клавиатура", "шт", 1, 2000),
        ("Сергеев", "Мышь", "шт", 1, 1500),
        ("Андреев", "Монитор", "шт", 1, 25000)
    ]
    
    try:
        cursor = conn.cursor()
        cursor.executemany('''
        INSERT INTO sales (buyer, item, unit, quantity, cost)
        VALUES (?, ?, ?, ?, ?)
        ''', sample_data)
        conn.commit()
        print("Добавлено 10 записей в таблицу 'sales'")
    except Error as e:
        print(f"Ошибка при вставке данных: {e}")

def search_records(conn):
    try:
        cursor = conn.cursor()

        print("\n1. Все покупки Иванова:")
        cursor.execute("SELECT * FROM sales WHERE buyer = 'Иванов'")
        print(cursor.fetchall())

        print("\n2. Товары дороже 10000:")
        cursor.execute("SELECT * FROM sales WHERE cost > 10000")
        print(cursor.fetchall())

        print("\n3. Товары, измеряемые в штуках:")
        cursor.execute("SELECT * FROM sales WHERE unit = 'шт'")
        print(cursor.fetchall())
        
    except Error as e:
        print(f"Ошибка при поиске данных: {e}")

def delete_records(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM sales WHERE buyer = 'Петров'")
        print("\n1. Удалены все покупки Петрова")

        cursor.execute("DELETE FROM sales WHERE cost < 1000")
        print("2. Удалены все товары дешевле 1000")

        cursor.execute("DELETE FROM sales WHERE unit = 'кг'")
        print("3. Удалены все товары, измеряемые в килограммах")
        
        conn.commit()
    except Error as e:
        print(f"Ошибка при удалении данных: {e}")
        conn.rollback()

def update_records(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("UPDATE sales SET cost = cost * 1.1 WHERE item = 'Ноутбук'")
        print("\n1. Стоимость ноутбуков увеличена на 10%")

        cursor.execute("UPDATE sales SET unit = 'упаковка' WHERE item = 'Кофе'")
        print("2. Единица измерения для кофе изменена на 'упаковка'")

        cursor.execute("UPDATE sales SET quantity = quantity * 2 WHERE quantity < 2")
        print("3. Количество товаров увеличено в 2 раза для записей с количеством меньше 2")
        
        conn.commit()
    except Error as e:
        print(f"Ошибка при обновлении данных: {e}")
        conn.rollback()

def print_all_records(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()
        
        print("\nТекущее состояние таблицы 'sales':")
        print("ID | Покупатель | Товар | Ед.изм | Количество | Стоимость")
        print("-" * 60)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
    except Error as e:
        print(f"Ошибка при выводе данных: {e}")

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        insert_sample_data(conn)

        print_all_records(conn)
        search_records(conn)
        delete_records(conn)
        update_records(conn)
        print_all_records(conn)
        
        conn.close()
        print("\nСоединение с SQLite закрыто")
    else:
        print("Не удалось установить соединение с базой данных")

if __name__ == '__main__':
    main()

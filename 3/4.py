import sqlite3


def create_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       full_name TEXT,
                       birth_year INTEGER,
                       occupation TEXT)''')
    connection.commit()
    connection.close()


def add_user(full_name, birth_year, occupation):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (full_name, birth_year, occupation) VALUES (?, ?, ?)",
                   (full_name, birth_year, occupation))
    connection.commit()
    connection.close()

def display_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Full Name: {user[1]}, Birth Year: {user[2]}, Occupation: {user[3]}")
    connection.close()

create_table()

while True:
    full_name = input("Введите ФИО (или 'стоп' для завершения): ")
    if full_name.lower() == 'стоп':
        break

    birth_year = int(input("Введите год рождения: "))
    occupation = input("Введите род деятельности: ")

    add_user(full_name, birth_year, occupation)

print("\nСодержимое базы данных:")
display_users()

from flask import Flask, render_template, request, redirect
import sqlite3
import random
import string

app = Flask(__name__)

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

def add_random_user():
    full_name = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    birth_year = random.randint(1980, 2000)
    occupation = "Random Occupation"
    
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (full_name, birth_year, occupation) VALUES (?, ?, ?)",
                   (full_name, birth_year, occupation))
    connection.commit()
    connection.close()

def delete_user(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    connection.commit()
    connection.close()

def get_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.close()
    return users

create_table()

@app.route('/')
def index():
    users = get_users()
    return render_template('index1.html', users=users)

@app.route('/add_random_user', methods=['POST'])
def add_random_user_route():
    add_random_user()
    return redirect('/')

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

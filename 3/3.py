from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Путь к файлу, в который будем записывать данные
file_path = 'data.txt'

# Домашняя страница с полем ввода и кнопко
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'content' in request.form:
        with open(file_path, 'a') as file:
            file.write(request.form['content'] + '\n')
    return redirect(url_for('index'))

@app.route('/view')
def view():
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return render_template('view.html', content=content)
    except FileNotFoundError:
        return "Файла еще нет"

if __name__ == '__main__':
    app.run(debug=True)

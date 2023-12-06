import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Калькулятор')

        self.input_line = QLineEdit(self)
        self.input_line.setReadOnly(True)
        self.input_line.setAlignment(2)  # Выравнивание текста по правому краю

        self.create_button('7')
        self.create_button('8')
        self.create_button('9')
        self.create_button('/')
        self.create_button('4')
        self.create_button('5')
        self.create_button('6')
        self.create_button('*')
        self.create_button('1')
        self.create_button('2')
        self.create_button('3')
        self.create_button('-')
        self.create_button('0')
        self.create_button('.')
        self.create_button('=')
        self.create_button('+')
        self.create_button('C')
        self.create_button('DEL')

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_line)

        button_grid = QGridLayout()
        button_grid.setSpacing(2)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'DEL'
        ]

        row = 0
        col = 0
        for button_text in buttons:
            button = self.create_button(button_text)
            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        vbox.addLayout(button_grid)
        self.setLayout(vbox)

        self.show()

    def create_button(self, text):
        button = QPushButton(text, self)
        button.clicked.connect(lambda: self.on_button_click(text))
        return button

    def on_button_click(self, button_text):
        current_text = self.input_line.text()

        if button_text == '=':
            try:
                result = str(eval(current_text))
                self.input_line.setText(result)
            except Exception as e:
                self.input_line.setText('Ошибка')
        elif button_text == 'C':
            self.input_line.clear()
        elif button_text == 'DEL':
            self.input_line.setText(current_text[:-1])
        else:
            self.input_line.setText(current_text + button_text)


def main():
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

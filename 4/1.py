import sys
from PyQt6.QtWidgets import QGridLayout, QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Калькулятор')

        self.input_line = QLineEdit(self)
        self.input_line.setReadOnly(True) 

        vbox = QVBoxLayout()
        vbox.addWidget(self.input_line)

        button_grid = QGridLayout()
        button_grid.setSpacing(2)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'DEL']
        ]


        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                button = self.create_button(buttons[i][j])
                button_grid.addWidget(button, i, j)
        

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
    CalculatorApp()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

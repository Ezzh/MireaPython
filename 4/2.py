import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QSlider, QRadioButton, QComboBox, QFileDialog, QTextBrowser

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Главное окно')

        self.height_label = QLabel('Рост:')
        self.height_slider = QSlider(1)  # Qt.Horizontal
        self.height_slider.setMinimum(140)
        self.height_slider.setMaximum(230)

        self.height_slider.valueChanged.connect(lambda: self.height_label.setText('Рост:' + str(self.height_slider.value()) + " см"))

        self.weight_label = QLabel('Вeс:')
        self.weight_slider = QSlider(1)  # Qt.Horizontal
        self.weight_slider.setMinimum(35)
        self.weight_slider.setMaximum(200)
        self.weight_slider.valueChanged.connect(lambda: self.weight_label.setText('Вес:' + str(self.weight_slider.value()) + " кг"))


        self.gender_label = QLabel('Пол:')
        self.male_radio = QRadioButton('М')
        self.female_radio = QRadioButton('Ж')

        self.age_label = QLabel('Возраст:')
        self.age_input = QLineEdit()

        self.name_label = QLabel('Имя:')
        self.name_input = QLineEdit()

        self.surname_label = QLabel('Фамилия:')
        self.surname_input = QLineEdit()

        self.patronymic_label = QLabel('Отчество:')
        self.patronymic_input = QLineEdit()

        self.occupation_label = QLabel('Род деятельности:')
        self.occupation_combobox = QComboBox()
        self.occupation_combobox.addItems(['Программист', 'Учитель', 'Врач', 'Инженер'])

        self.marital_status_label = QLabel('Семейное положение:')
        self.single_radio = QRadioButton('Свободен/на')
        self.in_relationship_radio = QRadioButton('В отношениях')

        self.save_button = QPushButton('Сохранить в файл')
        self.save_button.clicked.connect(self.save_to_file)

        self.view_button = QPushButton('Просмотр файла')
        self.view_button.clicked.connect(self.show_second_window)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.height_label)
        vbox.addWidget(self.height_slider)
        vbox.addWidget(self.weight_label)
        vbox.addWidget(self.weight_slider)
        vbox.addWidget(self.gender_label)
        vbox.addWidget(self.male_radio)
        vbox.addWidget(self.female_radio)
        vbox.addWidget(self.age_label)
        vbox.addWidget(self.age_input)
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.name_input)
        vbox.addWidget(self.surname_label)
        vbox.addWidget(self.surname_input)
        vbox.addWidget(self.patronymic_label)
        vbox.addWidget(self.patronymic_input)
        vbox.addWidget(self.occupation_label)
        vbox.addWidget(self.occupation_combobox)
        vbox.addWidget(self.marital_status_label)
        vbox.addWidget(self.single_radio)
        vbox.addWidget(self.in_relationship_radio)
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.view_button)

        self.setLayout(vbox)

        self.show()

    def save_to_file(self):
        data = {
            'Рост': self.height_slider.value(),
            'Вес': self.weight_slider.value(),
            'Пол': 'М' if self.male_radio.isChecked() else 'Ж',
            'Возраст': self.age_input.text(),
            'Имя': self.name_input.text(),
            'Фамилия': self.surname_input.text(),
            'Отчество': self.patronymic_input.text(),
            'Род деятельности': self.occupation_combobox.currentText(),
            'Семейное положение': 'Свободен/на' if self.single_radio.isChecked() else 'В отношениях'
        }

        file_path, _ = QFileDialog.getSaveFileName(self, 'Сохранить файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)')

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                for key, value in data.items():
                    file.write(f'{key}: {value}\n')

    def show_second_window(self):
        self.second_window = SecondApp()
        self.second_window.show()


class SecondApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Второе окно')

        self.text_browser = QTextBrowser()

        vbox = QVBoxLayout()
        vbox.addWidget(self.text_browser)

        self.setLayout(vbox)

        self.load_file_content()

    def load_file_content(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', 'Текстовые файлы (*.txt);;Все файлы (*)')

        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_browser.setPlainText(content)


def main():
    app = QApplication(sys.argv)
    MainApp()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

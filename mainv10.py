import random
import sys
import time

from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QMessageBox
from qt_material import apply_stylesheet
from PyQt5 import QtWidgets, QtCore

class Training2(QWidget):
    def __init__(self):
        super().__init__()

#Создание окна и его наименование
        self.setWindowTitle('Тренировка 2')
        self.setGeometry(630, 315, 640, 480)

#Строчки кода назначения переменных
        self.score = 0
        self.start_time = None
        self.end_time = None

#Надпись 'Счёт' в тренировке
        self.score_label = QLabel(self)
        self.score_label.setGeometry(10, 10, 100, 30)
        self.score_label.setText('Счёт: 0')
        self.score_label.setStyleSheet('font-size: 16px')

#Надпись Врменени в окне
        self.time_label = QLabel(self)
        self.time_label.setGeometry(270, 100, 300, 100)
        self.time_label.setStyleSheet('font-size: 16px')

        # Настройки кнопки Выход
        self.exitbutton = QPushButton('Выход', self)
        self.exitbutton.setGeometry(450, 400, 100, 50)
        self.exitbutton.clicked.connect(self.pressexit)

#Настройки кнопки Старт
        self.start_button = QPushButton('Старт', self)
        self.start_button.setGeometry(100, 400, 100, 50)
        self.start_button.clicked.connect(self.start_training)
        self.green_button = None
        self.show()

#Функция запуска тренировки
    def start_training(self):
        self.start_button.hide()
        self.exitbutton.hide()
        self.start_time = time.time()
        self.score = 0
        self.score_label.setText('Счёт: 0')
        self.time_label.setText('')
        self.create_button()

#Функция с условием. Если счёт меньше 30, то создаются зелёные кнопки, если нет то останавливается таймер и сама программа
    def create_button(self):
        if self.score < 30:
            button = QPushButton(self)
            x = random.randint(10, self.width() - 100)
            y = random.randint(10, self.height() - 100)
            button.setGeometry(x, y, 50, 50)
            button.show()
            button.setStyleSheet('background-color: green')
            button.clicked.connect(self.button_clicked)
            self.timer = QTimer(self)
            self.timer.setSingleShot(True)
            self.timer.timeout.connect(self.remove_button)
            self.timer.start(10000)
            self.green_button = button
            x = random.randint(10, self.width() - 100)
            y = random.randint(10, self.height() - 100)
            self.green_button.setGeometry(x, y, 50, 50)
        else:
            self.timer.stop()
            self.end_game()

#Функция которая создаёт кнопку в другом месте после нажатия
    def remove_button(self):
        if self.green_button:
            self.green_button.hide()
        self.create_button()

#Функция которая прибавляет очки за нажатие на зелёную кнопку
    def button_clicked(self):
        self.score += 1
        self.score_label.setText(f'Счёт: {self.score}')
        self.green_button.hide()
        self.create_button()

#Функция завершения программы. После того как пользователь набрал 30 очков на экран выводится время и кнопка Старт, с помощью которой можно начать тренировку заного
    def end_game(self):
        self.end_time = time.time()
        self.time_label.setText(f'Время: {self.end_time - self.start_time:.2f} сек')
        self.timer.stop()
        self.start_button.show()
        self.exitbutton.show()

#Функция, закрывающая окно
    def pressexit(self):
        self.train5 = MainWindow()
        self.close()
        self.train5.show()


class ReactionTraining(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = None
        self.start_time = None

#Настройки размера окна и его название
        self.setGeometry(630, 315, 640, 480)
        self.setWindowTitle('Приложение "Training reaction1"')

#Кнопка "Начать", которая запускает тренировку
        self.start_button = QPushButton('Начать', self)
        self.start_button.setGeometry(350, 400, 252, 52)
        self.start_button.clicked.connect(self.start_game)

        self.ex_button = QPushButton ('Выход', self)
        self.ex_button.setGeometry(40, 400, 252, 52)
        self.ex_button.clicked.connect(self.pressexit2)

#Настройки красной кнопки
        self.reaction_button = QPushButton(self)
        self.reaction_button.setGeometry(270, 190, 100, 100)
        self.reaction_button.hide()
        self.reaction_button.clicked.connect(self.check_reaction)

#Настройки надписей на экране
        self.result_label = QLabel(self)
        self.result_label.setGeometry(170, 190, 300, 100)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet('font-size: 16px')
        self.result_label.hide()

#Функция, которая работает на красной кнопке
    def start_game(self):
        self.start_button.hide()
        self.ex_button.hide()
        self.result_label.hide()
        self.reaction_button.show()
        self.reaction_button.setStyleSheet('background-color: red')
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(random.randint(1000, 5000))

#Функция, которая запускает таймер и при нажатии на зелёную кнопку останавливает таймер и выводит время на эран
    def change_color(self):
        self.reaction_button.setStyleSheet('background-color: green')
        self.start_time = QDateTime.currentDateTime()

#Функция с условием, которая перезапускает тренировку в том случае, если пользователь нажал на красную кнопку, а не на зелёную
    def check_reaction(self, event):
        if self.reaction_button.styleSheet() == 'background-color: red':
            self.result_label.setText('Слишком рано, попробуйте ещё раз')
        else:
            end_time = QDateTime.currentDateTime()
            reaction_time = self.start_time.msecsTo(end_time) / 1000
            self.result_label.setText(f'Ваше время: {reaction_time:.3f} сек')
        self.result_label.show()
        self.reaction_button.hide()
        self.start_button.show()
        self.ex_button.show()

#Функция, которая закрывает окно при нажатии кнопки Esc на клавиатуре
    def pressexit2(self):
        self.train5 = MainWindow()
        self.close()
        self.train5.show()
# кнопка ESC (выход из приложения)


#Класс, который создаёт главное меню
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

#Настройки размера окна
        self.resize(1920, 1080)
        self.setMinimumSize(QtCore.QSize(1920, 1080))
        self.setMaximumSize(QtCore.QSize(1920, 1080))
        self.setGeometry(1, 28, 1920, 1080)
        #  Окно Главного меню
        self.setWindowTitle('Главное меню')
        #  Текст в Окне "Главное меню"
        self.gl_text = QLabel(self)
        self.gl_text.setText("Главное меню")
        self.gl_text.setGeometry(865, 40, 275, 120)
        self.gl_text.setStyleSheet('font-size: 30pt;')
        #  Текст рядом с водом никнейма
        self.main_text = QLabel(self)
        self.main_text.setText("Введите имя: ")
        self.main_text.setGeometry(630, 250, 200, 27)
        self.main_text.setStyleSheet('font-size: 20pt;')
        #  Строчка для ввода никнейма

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(820, 224, 350, 70))
        self.lineEdit.setStyleSheet('font-size: 20pt;')

        #  Кнопка старт, которая привязана к другому классу и открывает новое окно с приложением
        self.button1 = QPushButton("Тренировка 1", self)
        self.button1.setGeometry(820, 340, 350, 70)
        self.button1.setStyleSheet('font-size: 15pt;')
        self.button1.clicked.connect(self.open_train_window)

        #  Кнопка, которая закрывает программу
        self.button2 = QPushButton("Выход", self)
        self.button2.setStyleSheet('font-size: 15pt;')
        self.button2.setGeometry(820, 500, 350, 70)
        self.button2.clicked.connect(self.exit_programm)

        # Кнопка, открывающая таблицу
        self.button3 = QPushButton("Тренировка 2", self)
        self.button3.setStyleSheet('font-size: 15pt;')
        self.button3.setGeometry(820, 420, 350, 70)
        self.button3.clicked.connect(self.open_train2_window)

#Функция с условием, к которой привязана кнопка, для запуска программы, если в главном меню не введено имя то тренировка не запустится
    def open_train_window(self):
        if self.lineEdit.text():
            self.train4 = ReactionTraining()
            self.close()
            self.train4.show()
        else:
            QMessageBox.question(self, 'Введите имя', "Для того, чтобы  начать  тренировку, нужно ввести имя пользователя",
                                 QMessageBox.Ok)

#Функция с условием, к которой привязана кнопка, для запуска программы, если в главном меню не введено имя то тренировка не запустится
    def open_train2_window(self):
        if self.lineEdit.text():
            self.train5 = Training2()
            self.close()
            self.train5.show()
        else:
            QMessageBox.question(self, 'Введите имя', "Для того, чтобы  начать  тренировку, нужно ввести имя пользователя",
                                 QMessageBox.Ok)

    # Функция,к которой привязана кнопка "Выход", при нажатии программа закрывается полностью
    def exit_programm(self):
        QApplication.quit()


#Условие, которое проверяет, запущен ли данный скрипт напрямую, или импортирован как модуль в другой скрипт. Используется для запуска приложения.
# Обычно, в этом блоке кода создаются экземпляры классов, которые наследуются от `QApplication` и `QWidget`, и вызывается метод `show()` для отображения окна приложения.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    # Для выбора шаблонов https://pypi.org/project/qt-material
    window.show()
    sys.exit(app.exec_())
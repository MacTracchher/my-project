import sys, random
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QCheckBox,
    QButtonGroup,
)


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Авторизация")

        self.lblLogin = QLabel("Введи логин")
        self.edtLogin = QLineEdit("user")
        self.lblPassword = QLabel("Введи пароль")
        self.edtPassword = QLineEdit("user")
        self.btnAuth = QPushButton("Войти")

        layout = QVBoxLayout()
        layout.addWidget(self.lblLogin)
        layout.addWidget(self.edtLogin)
        layout.addWidget(self.lblPassword)
        layout.addWidget(self.edtPassword)
        layout.addWidget(self.btnAuth)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnAuth.clicked.connect(
            lambda: self.true_auth(self.edtLogin.text(), self.edtPassword.text())
        )

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def true_auth(self, login, password):
        if login == "user" and password == "user":
            self.quest1Window = Quest1Window()
            self.quest1Window.show()
            self.close()
        else:
            self.capchaWindow = CapchaWindow()
            self.capchaWindow.show()
            self.close()


class Quest1Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTest1 = QLabel("Вопрос №1")
        self.btnTestNext1 = QPushButton("Ответит")

        self.btnTestCheck11 = QCheckBox("1")
        self.btnTestCheck21 = QCheckBox("2")
        self.btnTestCheck31 = QCheckBox("3")

        self.btnGroup1 = QButtonGroup()
        self.btnGroup1.addButton(self.btnTestCheck11)
        self.btnGroup1.addButton(self.btnTestCheck21)
        self.btnGroup1.addButton(self.btnTestCheck31)

        layout = QVBoxLayout()
        layout.addWidget(self.lblTest1)
        layout.addWidget(self.btnTestCheck11)
        layout.addWidget(self.btnTestCheck21)
        layout.addWidget(self.btnTestCheck31)
        layout.addWidget(self.btnTestNext1)

        self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnTestNext1.clicked.connect(self.quest_next1)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def quest_next1(self):
        self.quest2 = Quest2Window()
        self.quest2.show()
        self.close()


class Quest2Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTest2 = QLabel("Вопрос №2")
        self.btnTestNext2 = QPushButton("Ответит")
        self.btnTestBack2 = QPushButton("Назад")

        self.btnTestCheck12 = QCheckBox("1")
        self.btnTestCheck22 = QCheckBox("2")
        self.btnTestCheck32 = QCheckBox("3")

        self.btnGroup2 = QButtonGroup()
        self.btnGroup2.addButton(self.btnTestCheck12)
        self.btnGroup2.addButton(self.btnTestCheck22)
        self.btnGroup2.addButton(self.btnTestCheck32)

        layout = QVBoxLayout()
        layout.addWidget(self.lblTest2)
        layout.addWidget(self.btnTestCheck12)
        layout.addWidget(self.btnTestCheck22)
        layout.addWidget(self.btnTestCheck32)
        layout.addWidget(self.btnTestNext2)
        layout.addWidget(self.btnTestBack2)

        self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnTestNext2.clicked.connect(self.quest_next2)
        self.btnTestBack2.clicked.connect(self.quest_back2)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def quest_next2(self):
        self.quest3 = Quest3Window()
        self.quest3.show()
        self.close()

    def quest_back2(self):
        self.quest1 = Quest1Window()
        self.quest1.show()
        self.close()


class Quest3Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTest3 = QLabel("Вопрос №3")
        self.btnTestNext3 = QPushButton("Ответит")
        self.btnTestBack3 = QPushButton("Назад")

        self.btnTestCheck13 = QCheckBox("1")
        self.btnTestCheck23 = QCheckBox("2")
        self.btnTestCheck33 = QCheckBox("3")

        self.btnGroup3 = QButtonGroup()
        self.btnGroup3.addButton(self.btnTestCheck13)
        self.btnGroup3.addButton(self.btnTestCheck23)
        self.btnGroup3.addButton(self.btnTestCheck33)

        layout = QVBoxLayout()
        layout.addWidget(self.lblTest3)
        layout.addWidget(self.btnTestCheck13)
        layout.addWidget(self.btnTestCheck23)
        layout.addWidget(self.btnTestCheck33)
        layout.addWidget(self.btnTestNext3)
        layout.addWidget(self.btnTestBack3)

        self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnTestNext3.clicked.connect(self.quest_next3)
        self.btnTestBack3.clicked.connect(self.quest_back3)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def quest_next3(self):
        self.questF = TestFinishWindow()
        self.questF.show()
        self.close()

    def quest_back3(self):
        self.quest2 = Quest2Window()
        self.quest2.show()
        self.close()


class TestFinishWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTestF = QLabel("Тест пройден")

        layout = QVBoxLayout()
        layout.addWidget(self.lblTestF)

        self.setLayout(layout)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())


class CapchaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Капча")

        self.lblCapcha = QLabel("Введи капчу:")
        self.rmdCapcha = QLabel(str(random.randint(1000, 9999)))
        self.edtCapcha = QLineEdit()
        self.btnCapcha = QPushButton("Подтвердить")
        self.lockout = 0
        self.timeout = 3

        layout = QVBoxLayout()
        layout.addWidget(self.lblCapcha)
        layout.addWidget(self.rmdCapcha)
        layout.addWidget(self.edtCapcha)
        layout.addWidget(self.btnCapcha)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnCapcha.clicked.connect(
            lambda: self.true_capcha(self.edtCapcha.text(), self.rmdCapcha.text())
        )

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def true_capcha(self, introCapcha, generCapcha):
        if introCapcha == generCapcha:
            self.authWindow = AuthWindow()
            self.authWindow.show()
            self.close()
        elif self.lockout == 2:
            self.timer = QTimer()
            self.timer.start(1000)
            self.btnCapcha.setDisabled(True)
            self.lblCapcha.setText("Блокировка: 3 сек!")
            self.timer.timeout.connect(self.timer_tick)
        else:
            self.lockout += 1

    def timer_tick(self):
        self.timeout -= 1
        self.lblCapcha.setText(f"Блокировка: {self.timeout} сек!")
        if self.timeout == 0:
            self.lockout = 0
            self.timeout = 3
            self.timer.stop()
            self.btnCapcha.setDisabled(False)
            self.lblCapcha.setText("Введи капчу:")


app = QApplication(sys.argv)
authWindow = AuthWindow()
authWindow.show()
sys.exit(app.exec())

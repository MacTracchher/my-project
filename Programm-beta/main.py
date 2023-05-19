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
)


class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Авторизация")

        self.lblLogin = QLabel("Введи логин")
        self.edtLogin = QLineEdit()
        self.lblPassword = QLabel("Введи пароль")
        self.edtPassword = QLineEdit()
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
            self.ownWindow = OwnWindow()
            self.ownWindow.show()
            self.close()
        else:
            self.capchaWindow = CapchaWindow()
            self.capchaWindow.show()
            self.close()


class OwnWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Главная панель")

        self.hello = QLabel("hello")

        layout = QVBoxLayout()
        layout.addWidget(self.hello)

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

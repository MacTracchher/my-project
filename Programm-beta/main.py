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
    QRadioButton,
    QCheckBox,
    QGroupBox,
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
    results = [0, 0]

    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTest1 = QLabel("Вопрос №1")
        self.btnTestNext1 = QPushButton("Ответит")

        self.btnTestCheck11 = QRadioButton("1")
        self.btnTestCheck21 = QRadioButton("2")
        self.btnTestCheck31 = QRadioButton("3")

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

        self.btnTestNext1.clicked.connect(self.next_clicked1)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def next_clicked1(self):
        if self.btnTestCheck11.isChecked():
            self.results[0] += 100
        self.quest2Window = Quest2Window(self.results)
        self.quest2Window.show()
        self.close()


class Quest2Window(QMainWindow):
    def __init__(self, results):
        super().__init__()

        self.results = results

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.lblTest2 = QLabel("Вопрос №2")
        self.btnTestNext2 = QPushButton("Ответит")
        self.btnTestBack2 = QPushButton("Назад")

        self.btnTestCheck12 = QCheckBox("1")
        self.btnTestCheck22 = QCheckBox("2")
        self.btnTestCheck32 = QCheckBox("3")

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

        self.btnTestNext2.clicked.connect(self.next_clicked2)
        self.btnTestBack2.clicked.connect(self.back_clicked)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def next_clicked2(self):
        if self.btnTestCheck12.isChecked():
            self.results[1] += 50
        if self.btnTestCheck22.isChecked():
            self.results[1] += 50
        if self.btnTestCheck32.isChecked():
            self.results[1] -= 50
        if self.results[1] < 0:
            self.results[1] = 0
        j = 0
        for i in self.results:
            if i == 100:
                j += 2
            elif i == 50:
                j += 1
        self.testFinishWindow = TestFinishWindow(str(j), self.results)
        self.testFinishWindow.show()
        self.close()

    def back_clicked(self):
        self.results[0] = 0
        self.quest1Window = Quest1Window()
        self.quest1Window.show()
        self.close()


class TestFinishWindow(QMainWindow):
    def __init__(self, result, bal):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Тест")

        self.bal = bal
        self.result = result

        self.txt = QLabel("<center>Тест пройден</center>")
        self.txt1 = QLabel(f"<center>Вы набрали {result} из 4 баллов</center>")
        self.btn = QPushButton("Записать результаты в файл")

        gb = QGroupBox("Смотреть результаты")
        self.gb_lbl1 = QLabel(f"Вопрос 1: {int(bal[0]/50)} б.")
        self.gb_lbl2 = QLabel(f"Вопрос 2: {int(bal[1]/50)} б.")

        vbox_group = QVBoxLayout()
        vbox_group.addWidget(self.gb_lbl1)
        vbox_group.addWidget(self.gb_lbl2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.txt)
        vbox.addWidget(self.txt1)
        vbox.addWidget(gb)
        vbox.addWidget(self.btn)

        widget = QWidget()
        widget.setLayout(vbox)
        gb.setLayout(vbox_group)
        self.setCentralWidget(widget)

        self.btn.clicked.connect(self.write_res_clicked)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def write_res_clicked(self):
        resultat = f"Результаты \n Вы набрали {self.result} из 4 баллов \n Вопрос 1: {int(self.bal[0]/50)} \n Вопрос 2: {int(self.bal[1]/50)}"
        with open("results.txt", "w", encoding="utf-8") as res:
            res.write(resultat)


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

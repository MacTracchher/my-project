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

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblLogin)
        vbox.addWidget(self.edtLogin)
        vbox.addWidget(self.lblPassword)
        vbox.addWidget(self.edtPassword)
        vbox.addWidget(self.btnAuth)

        widget = QWidget()
        widget.setLayout(vbox)
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

        self.lblQuest_1 = QLabel("Вопрос №1")
        self.btnQuestNext_1 = QPushButton("Ответит")

        self.rbAnswer1_quest1 = QRadioButton("1")
        self.rbAnswer2_quest1 = QRadioButton("2")
        self.rbAnswer3_quest1 = QRadioButton("3")

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblQuest_1)
        vbox.addWidget(self.rbAnswer1_quest1)
        vbox.addWidget(self.rbAnswer2_quest1)
        vbox.addWidget(self.rbAnswer3_quest1)
        vbox.addWidget(self.btnQuestNext_1)

        self.setLayout(vbox)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.btnQuestNext_1.clicked.connect(self.next_quest_1)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def next_quest_1(self):
        if self.rbAnswer1_quest1.isChecked():
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

        self.lblQuest_2 = QLabel("Вопрос №2")
        self.btnQuestNext_2 = QPushButton("Ответит")
        self.btnQuestBack = QPushButton("Назад")

        self.cbAnswer1_quest2 = QCheckBox("1")
        self.cbAnswer2_quest2 = QCheckBox("2")
        self.cbAnswer3_quest2 = QCheckBox("3")

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblQuest_2)
        vbox.addWidget(self.cbAnswer1_quest2)
        vbox.addWidget(self.cbAnswer2_quest2)
        vbox.addWidget(self.cbAnswer3_quest2)
        vbox.addWidget(self.btnQuestNext_2)
        vbox.addWidget(self.btnQuestBack)

        self.setLayout(vbox)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.btnQuestNext_2.clicked.connect(self.next_quest_2)
        self.btnQuestBack.clicked.connect(self.back_quest)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def next_quest_2(self):
        if self.cbAnswer1_quest2.isChecked():
            self.results[1] += 50
        if self.cbAnswer2_quest2.isChecked():
            self.results[1] += 50
        if self.cbAnswer3_quest2.isChecked():
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

    def back_quest(self):
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

        self.lblTestFinish = QLabel("<center>Тест пройден</center>")
        self.lblTestResult = QLabel(f"<center>Вы набрали {result} из 4 баллов</center>")
        self.btnWrite = QPushButton("Записать результаты в файл")

        gbox = QGroupBox("Смотреть результаты")
        self.lblQuestResult_1 = QLabel(f"Вопрос 1: {int(bal[0]/50)} б.")
        self.lblQuestResult_2 = QLabel(f"Вопрос 2: {int(bal[1]/50)} б.")

        vboxGroup = QVBoxLayout()
        vboxGroup.addWidget(self.lblQuestResult_1)
        vboxGroup.addWidget(self.lblQuestResult_2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblTestFinish)
        vbox.addWidget(self.lblTestResult)
        vbox.addWidget(gbox)
        vbox.addWidget(self.btnWrite)

        widget = QWidget()
        widget.setLayout(vbox)
        gbox.setLayout(vboxGroup)
        self.setCentralWidget(widget)

        self.btnWrite.clicked.connect(self.write_result)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def write_result(self):
        resultat = f"Результаты \n Вы набрали {self.result} из 4 баллов \n Вопрос 1: {int(self.bal[0]/50)} \n Вопрос 2: {int(self.bal[1]/50)}"
        with open("results.txt", "w", encoding="utf-8") as res:
            res.write(resultat)
        self.close()


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

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblCapcha)
        vbox.addWidget(self.rmdCapcha)
        vbox.addWidget(self.edtCapcha)
        vbox.addWidget(self.btnCapcha)

        widget = QWidget()
        widget.setLayout(vbox)
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

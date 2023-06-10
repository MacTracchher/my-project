import random, sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
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
        self.setWindowTitle("Auth")

        vbox = QVBoxLayout()
        lblLogin = QLabel("Введи логин")
        edtLogin = QLineEdit("user")
        lblPassword = QLabel("Введи пароль")
        edtPassword = QLineEdit("user")
        btnAuth = QPushButton("Войти")

        vbox.addWidget(lblLogin)
        vbox.addWidget(edtLogin)
        vbox.addWidget(lblPassword)
        vbox.addWidget(edtPassword)
        vbox.addWidget(btnAuth)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        btnAuth.clicked.connect(
            lambda: self.true_auth(edtLogin.text(), edtPassword.text())
        )

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def true_auth(self, login, password):
        if login == "user" and password == "user":
            self.test1 = QuestWindowOne()
            self.test1.show()
            self.close()
        else:
            self.capcha = CapchaWindow()
            self.capcha.show()
            self.close()


class QuestWindowOne(QMainWindow):
    results = [0, 0]

    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Test")

        vbox = QVBoxLayout()
        lblQuest_1 = QLabel("Вопрос №1")
        btnQuestNext_1 = QPushButton("Ответить")
        rbAnswer1_quest1 = QRadioButton("1")
        rbAnswer2_quest1 = QRadioButton("2")
        rbAnswer3_quest1 = QRadioButton("3")

        vbox.addWidget(lblQuest_1)
        vbox.addWidget(rbAnswer1_quest1)
        vbox.addWidget(rbAnswer2_quest1)
        vbox.addWidget(rbAnswer3_quest1)
        vbox.addWidget(btnQuestNext_1)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        btnQuestNext_1.clicked.connect(lambda: self.next_quest_1(rbAnswer1_quest1))

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

    def next_quest_1(self, true):
        if true.isChecked():
            self.results[0] += 100
        self.test2 = QuestWindowTwo(self.results)
        self.test2.show()
        self.close()


class QuestWindowTwo(QMainWindow):
    def __init__(self, results):
        super().__init__()

        self.results = results

        self.resize(300, 200)
        self.setWindowTitle("Test")

        vbox = QVBoxLayout()
        lblQuest_2 = QLabel("Вопрос №2")
        btnQuestNext_2 = QPushButton("Ответит")
        btnQuestBack = QPushButton("Назад")
        cbAnswer1_quest2 = QCheckBox("1")
        cbAnswer2_quest2 = QCheckBox("2")
        cbAnswer3_quest2 = QCheckBox("3")

        vbox.addWidget(lblQuest_2)
        vbox.addWidget(cbAnswer1_quest2)
        vbox.addWidget(cbAnswer2_quest2)
        vbox.addWidget(cbAnswer3_quest2)
        vbox.addWidget(btnQuestNext_2)
        vbox.addWidget(btnQuestBack)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

        btnQuestNext_2.clicked.connect(
            lambda: self.next_quest_2(
                cbAnswer1_quest2, cbAnswer2_quest2, cbAnswer3_quest2
            )
        )
        btnQuestBack.clicked.connect(self.back_quest)

    def next_quest_2(self, answer_1, answer_2, answer_3):
        if answer_1.isChecked():
            self.results[1] += 50
        if answer_2.isChecked():
            self.results[1] += 50
        if answer_3.isChecked():
            self.results[1] -= 50
        if self.results[1] < 0:
            self.results[1] = 0
        j = 0
        for i in self.results:
            if i == 100:
                j += 2
            elif i == 50:
                j += 1
        self.finish = FinishTestWindow(str(j), self.results)
        self.finish.show()
        self.close()

    def back_quest(self):
        self.results[0] = 0
        self.test1 = QuestWindowOne()
        self.test1.show()
        self.close()


class FinishTestWindow(QMainWindow):
    def __init__(self, results, bal):
        super().__init__()

        self.results = results
        self.bal = bal

        self.resize(300, 200)
        self.setWindowTitle("Test")

        vbox = QVBoxLayout()
        vboxGroup = QVBoxLayout()
        lblTestFinish = QLabel("<center>Тест пройден</center>")
        lblTestResult = QLabel(f"<center>Вы набрали {results} из 4 баллов</center>")
        gbox = QGroupBox("Смотреть результаты")
        lblQuestResult_1 = QLabel(f"Вопрос 1: {int(bal[0]/50)} б.")
        lblQuestResult_2 = QLabel(f"Вопрос 2: {int(bal[1]/50)} б.")
        btnWrite = QPushButton("Записать результаты в файл")

        vboxGroup.addWidget(lblQuestResult_1)
        vboxGroup.addWidget(lblQuestResult_2)
        vbox.addWidget(lblTestFinish)
        vbox.addWidget(lblTestResult)
        vbox.addWidget(gbox)
        vbox.addWidget(btnWrite)

        widget = QWidget()
        widget.setLayout(vbox)
        gbox.setLayout(vboxGroup)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

        btnWrite.clicked.connect(self.write_result)

    def write_result(self):
        resultat = f"Результаты \n Вы набрали {self.results} из 4 баллов \n Вопрос 1: {int(self.bal[0]/50)} \n Вопрос 2: {int(self.bal[1]/50)}"
        with open("resultat.txt", "w", encoding="utf-8") as res:
            res.write(resultat)
        self.close()


class CapchaWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300, 200)
        self.setWindowTitle("Capcha")

        vbox = QVBoxLayout()
        self.lblCapcha = QLabel("Введи капчу:")
        rmdCapcha = QLabel(str(random.randint(1000, 9999)))
        edtCapcha = QLineEdit()
        self.btnCapcha = QPushButton("Подтвердить")
        self.lockout = 0
        self.timeout = 3

        vbox.addWidget(self.lblCapcha)
        vbox.addWidget(rmdCapcha)
        vbox.addWidget(edtCapcha)
        vbox.addWidget(self.btnCapcha)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            widget.setStyleSheet(css.read())

        self.btnCapcha.clicked.connect(
            lambda: self.true_capcha(edtCapcha.text(), rmdCapcha.text())
        )

    def true_capcha(self, introCapcha, generCapcha):
        if introCapcha == generCapcha:
            self.auth = AuthWindow()
            self.auth.show()
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
main = AuthWindow()
main.show()
sys.exit(app.exec())

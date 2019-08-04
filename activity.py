from PyQt5 import QtCore, QtGui, QtWidgets

from login import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.login_Button.clicked.connect(self.login)

    def login(self):
        id_name = self.id_name.text()
        id_pswd = self.id_pswd.text()
        if id_name == '123' and id_pswd == '123':
            self.log_text.append('登录成功')
            # self.log_text.setText('登录成功')
        else:
            # self.log_text.append('登录失败，请检查用户、密码')
            self.log_text.setText('登录失败，请检查用户、密码')

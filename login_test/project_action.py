# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from login_test.Project_test import Ui_MainWindow
from logs import log, file_path


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        log(file_path, '日志地址：{}'.format(file_path))
        self.login_Button.clicked.connect(self.login)

    def login(self):
        login_usr = self.login_usr.text()
        login_pwd = self.login_pwd.text()
        if login_usr == '123' and login_pwd == '123':
            log(file_path, '登录成功')
            # self.log_text.append('登录成功')
            # self.log_text.setText('登录成功')
        else:
            log(file_path, '登录失败，请检查用户、密码')
            # self.log_text.append('登录失败，请检查用户、密码')
            # self.log_text.setText('登录失败，请检查用户、密码')
        self.print_logs()

    def print_logs(self):
        # print("重新读取文件({}秒)：".format(n))
        print("清空输出")
        self.login_log.clear()
        for line in open(file_path):
            line = line.rstrip()
            print("打印输出：{}".format(line))
            self.login_log.append(line)

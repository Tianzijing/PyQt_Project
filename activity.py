# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

from login import Ui_MainWindow
from logs import log, file_path


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        log(file_path, '{}'.format(file_path))
        self.login_Button.clicked.connect(self.login)

    def login(self):
        id_name = self.id_name.text()
        id_pswd = self.id_pswd.text()
        if id_name == '123' and id_pswd == '123':
            log(file_path, '登录成功')
            # self.log_text.append('登录成功')
            # self.log_text.setText('登录成功')
        else:
            log(file_path, '登录失败，请检查用户、密码')
            # self.log_text.append('登录失败，请检查用户、密码')
            # self.log_text.setText('登录失败，请检查用户、密码')

    def print_logs(self):
        # print("重新读取文件({}秒)：".format(n))
        print "清空输出"
        self.log_text.clear()
        for line in open(file_path):
            print "打印输出"
            # print line,  #python2 用法
            self.log_text.append(line[:-1])
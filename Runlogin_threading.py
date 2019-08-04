# -*- coding: utf-8 -*-
import sys
import threading
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal

from activity import MainWindow

# class WorkThread(QThread):
#     trigger = pyqtSignal()
#
#     def __int__(self):
#         super(WorkThread, self).__init__()
#
#     def run(self):
#         # for i in range(20000):
#         #     for j in range(100000):
#         #         pass
#         mainWindow.show()
#         sys.exit(app.exec_())
#
#         # 循环完毕后发出信号
#         self.trigger.emit()

def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # mainWindow.print_logs()
    # work(mainWindow)
    sys.exit(app.exec_())

# def work(mainWindow):
#     timer = QTimer()
#     # 计时器每秒计数
#     timer.start(1000)
#     # 每次计时结束，触发 countTime
#     timer.timeout.connect(lambda:mainWindow.print_logs())

if __name__ == "__main__":
    show_MainWindow()
    # app = QtWidgets.QApplication(sys.argv)
    # mainWindow = MainWindow()
    # mainWindow.show()
    # work(mainWindow)
    # sys.exit(app.exec_())

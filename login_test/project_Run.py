# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets

from login_test.project_action import MainWindow


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    show_MainWindow()

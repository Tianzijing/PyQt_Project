#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from time import sleep

from logs import log, get_log_path

exitFlag = 0

file_path = get_log_path(__file__, __name__)


class myThread_1(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, time):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.time = time

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        tp.__init__(self.time)


class myThread_2(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, time):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.time = time

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        tp.log_print(self.time)


class test_ptiny():

    # def print_time(self, time):
    def __init__(self, time):
        n = 0
        for i in range(400):
            sleep(time)
            n += time
            log(file_path, "秒数：{}".format(n))

    def log_print(self, time):
        n = 0
        for i in range(400):
            sleep(time)
            n += time
            print("重新读取文件({}秒)：".format(n))
            for line in open(file_path):
                # print line,  #python2 用法
                print(line[:-1])

tp = test_ptiny(5)
t1 = myThread_1('T1', 5)
t2 = myThread_2('T2', 8)
t1.start()
t2.start()

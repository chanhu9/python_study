#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/29 20:49

import threading
import time
import os

locks = threading.Lock()
locks.acquire()

locks.release()

def dance(name):
    print("========开始跳舞========")
    print(threading.current_thread())
    # print(os.getpid())
    # print(os.getppid())

    for i in range(4):
        print(f"{name}正在跳舞....")
        time.sleep(0.5)


def sing(name):
    print("========开始唱儿歌========")
    print(threading.current_thread())
    # print(os.getpid())
    # print(os.getppid())

    for i in range(4):
        print(f"{name}正在唱歌....")
        time.sleep(0.5)

if __name__ == '__main__':
    dance_hu = threading.Thread(group=None, target=dance, name="dance_hu", args=("hu",))
    sing_yu = threading.Thread(group=None, target=sing, name="sing_yu", kwargs={"name":"yu"})
    dance_hu.setDaemon(True)
    sing_yu.setDaemon(True)

    dance_hu.start()
    sing_yu.start()


    print("要结束了")
    exit()

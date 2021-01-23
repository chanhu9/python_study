#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/29 20:00

import multiprocessing
import time
import os

my_list = []
def dance(name):
    print("========开始跳舞=========")
    print(os.getpid())
    print(os.getppid())

    for i in range(5):

        # time.sleep(2)
        print(f"{name}正在跳舞....")
        os.kill(os.getpid(), 9)

def sing(name):
    print("========开始唱歌========")
    print(os.getpid())
    print(os.getppid())
    for i in range(20):
        my_list.append(i)
        time.sleep(0.5)
        print(f"{name}正在唱歌....")
    print(my_list)



if __name__ == '__main__':
    dance_li = multiprocessing.Process(group=None, target=dance, name="dance", args=("li",))
    sing_hu = multiprocessing.Process(group=None, target=sing, name="sing", kwargs={"name":"hu"})
    print("=======主线程=========")
    print(multiprocessing.current_process())
    print(os.getpid())
    print(os.getppid())

    # sing_hu.daemon = True
    dance_li.start()
    sing_hu.start()
    print(my_list)
    sing_hu.terminate()

    exit()
#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/30 15:01

import threading
import time

lock = threading.Lock()
lock2 = threading.RLock()

num = 0
class ThreadTest(threading.Thread):


    def __init__(self, name):
        super().__init__(name=name)

    # #
    # def run(self):
    #     global num
    #     # lock.acquire()
    #     lock.acquire()
    #     # print(f"{self.name}=====hahaha")
    #     num += 1
    #
    #     time.sleep(0.5)
    #     # lock.release()
    #     print(num)
    #     lock.release()



    def run(self):
        global num

        lock2.acquire()
        lock2.acquire()
        for i in range(10):
            num += 1
        # print(f"{self.name}=====hahaha")
        print(num)
        lock2.release()
        lock2.release()



if __name__ == '__main__':
    thread_list = []
    for i in range(5):
        thread_list.append(ThreadTest(str(i)))
    print("start")
    for threads in thread_list:
        threads.start()
        # print(threads.name)

    for i in thread_list:
        i.join()

    print("end")
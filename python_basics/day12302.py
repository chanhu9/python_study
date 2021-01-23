#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/30 19:25

import threading
import time


def run2():
    cond.acquire()
    print("李白：集合，到我这里来")
    cond.wait()

    print("李白：好的，我等你")
    cond.notify(n=1)

    cond.release()


def run3():
    # time.sleep(2)
    cond.acquire()
    print("孙尚香:收到，等我集合打团")
    cond.notify(n=1)
    cond.wait()

    print("孙尚香：我已到达，发起进攻")

    # cond.release()



# class ThreadCondition(threading.Thread):
#
#     def __init__(self, name):
#         super().__init__(name=name)
#
#
#     def run(self, fun):
#         fun()




if __name__ == '__main__':

    cond = threading.Condition()

    thread_1 = threading.Thread(target=run2)
    thread_11 = threading.Thread(target=run2)
    # thread_12 = threading.Thread(target=run2)
    #
    thread_2 = threading.Thread(target=run3)

    thread_1.start()
    thread_11.start()
    # thread_12.start()
    thread_2.start()

    thread_1.join()
    thread_11.join()
    # thread_12.join()
    thread_2.join()







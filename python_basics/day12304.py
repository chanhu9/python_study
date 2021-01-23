#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/30 20:37

import threading
import time


class ThreadEvent(threading.Thread):

    def __init__(self, name):
        super().__init__(name=name)


    def run(self):
        print("start........")
        event.wait()
        # time.sleep(1)
        print(event.is_set())
        print("线程不阻射，继续执行")



if __name__ == '__main__':
    event = threading.Event()
    thread_1 = ThreadEvent("hjc")

    thread_1.start()
    time.sleep(2)
    event.set()

    print("over")






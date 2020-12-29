#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/25 18:43

import time
import threading



class DayThreads(threading.Thread):

    def __init__(self, threadname):
        threading.Thread.__init__(self, name="线程" + threadname)


    def run(self):
        time.sleep(2)
        print("hello world")
        print(f"{self.name}:now timestamp is {time.time()}")



if __name__ == '__main__':
    threadlist = []

    for i in range(4):
        threadlist.append(DayThreads(str(i)))

    for i in threadlist:
        i.start()




    for i in threadlist:
        i.join()

    print("end")
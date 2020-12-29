#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/28 20:53

class Srudents:

    age = "未成年"
    __achool = "一中"

    def __init__(self):
        self.name = "小伙子"

    def study(self):
        print("学习认真")

    @classmethod
    def set_age(cls, num):
        cls.age = num

    @staticmethod
    def view():
        print("这个是访问")



if __name__ == '__main__':
    hjc = Srudents()
    cmd = Srudents()

    hjc.set_age(30)
    print(hjc.age)
    print(Srudents.age)
    hjc.view()
    Srudents.view()



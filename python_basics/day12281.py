#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/28 20:31

__all__ = ["A", "B"]
class A(object):
    """
    这里是主食
    """

    def __init__(self):
        self.name = "A"

    def work(self):
        print("慢悠悠的工作")


class B(A):

    def work(self):
        print("非常拼命的工作")


class D(A):

    def work(self):
        print("家里躺尸，不用工作")


class GongS:

    def make(self,peo):
        peo.work()

if __name__ == '__main__':

    b = B()
    d = D()
    g = GongS()
    g.make(b)
    g.make(d)

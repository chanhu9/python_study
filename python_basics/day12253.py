#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/25 19:32

class A(object):

    def __init__(self):
        self.name = "A"

    def __str__(self):
        return "这个是A"

    def make(self):
        print(f"这个是{self.name}")


class D(object):

    def __init__(self):
        self.name = "D"


    def make(self):
        print(f"这个是{self.name}")

    def __str__(self):
        return "这个是D"


class B(D,A):

    def __init__(self):
        self.name = "B"

    def make(self):
        B.__init__(self)
        print(f"这个是{self.name}")

    def make_A(self):
        A.__init__(self)
        A.make(self)

    def make_D(self):
        D.__init__(self)
        D.make(self)

class G(B):
    pass



if __name__ == '__main__':
 b = B()
 b.make_A()
 b.make_D()
 b.make()
 print(b.name)
 print(G.__mro__)
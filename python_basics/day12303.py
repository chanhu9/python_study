#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/30 19:29

class A(object):

    def __init__(self, name):
        self.name = name
        self.age = 18
        self.sex = "男"


    def run(self):
        print(self.name, self.age,self.sex)



class B(A):

    def __init__(self, name,heigh, high):
        super().__init__(name=name)
        self.heigh = heigh
        self.high = high
        # self.name = name


    def run2(self):
        print(self.high,self.heigh)


if __name__ == '__main__':
    b = B("haha", 178, 70)
    b.run2()
    # print(b.name)
    b.run()





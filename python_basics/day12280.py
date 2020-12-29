#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/28 17:53

class A(object):

    def __init__(self):
        self.name = "A"

    def make(self):
        print(f"这里是{self.name}")


class B(A):

    def __init__(self):
        super().__init__()
        self.name = "B"
        self.__money = "20000"

    def make(self):
        print(f"这里是{self.name}")
        super().__init__()
        # print(f"这里是{# self.name}")
        super().make()

    def __caifu(self):
        print(f"我这里有{self.__money}")

    def get_caifu(self):
        self.__caifu()

    def set_caifu(self, num):
        self.__money = num





class D(B):

    def __init__(self):
        # super.__init__()
        self.name ="D"

    def make(self):
        self.__init__()
        print(f"这里是{self.name}")

    # def make_B(self):
    #     B.__init__(self)
    #     print(f"这里是{self.name}")

    def make_A(self):
        print(f"这里是{self.name}")
        super().__init__()
        super().make()





if __name__ == '__main__':
    d = D()
    d.make_A()
    d.get_caifu()
    d.set_caifu(5555)
    d.get_caifu()
    # d.make_B()
    d.make()

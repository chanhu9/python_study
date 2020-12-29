#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/25 19:03

class BoyFriend:

    def __init__(self, name):
        self.name = name


    def __str__(self):
        # print(self)
        return "这个是对象的内存地址"


    def __del__(self):

        print(f"{self}对象已经被删除")

    # def get_address(self):
    #     print(self)


if __name__ == '__main__':
    bf = BoyFriend("hjc")
    # bf.get_address()
    print(bf)
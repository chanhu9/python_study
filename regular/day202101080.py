#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 16:05


class Person:

    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return  self.__age


    @age.setter
    def age(self, new_age):
        if new_age > 18:
            print("成精了")

        else:
            self.__age = new_age


if __name__ == '__main__':
    hjc = Person()
    res = hjc.age
    print(res)
    hjc.age = 16
    print(hjc.age)
    hjc.age = 100
    print(hjc.age)

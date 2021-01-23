#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 16:25

class Person(object):

    def __init__(self):
        self.__age = 20


    def get_age(self):
        return self.__age


    def set_age(self, new_age):
        if new_age > 80:
            print("太老了")

        else:
            self.__age = new_age


    age = property(get_age, set_age)


hjc = Person()
print(hjc.age)
hjc.age = 100
print(hjc.age)
hjc.age = 30
print(hjc.age)
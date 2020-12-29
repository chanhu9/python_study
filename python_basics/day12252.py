#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/25 19:14

class Furniture:

    def __init__(self, name, size):
        self.name = name
        self.size = size



class Room:

    def __init__(self):
        self.area = 120
        self.spacearea = 120
        self.jiaju = []


    def add(self, furn):
        self.jiaju.append(furn.name)
        self.spacearea = self.spacearea - furn.size

    def __str__(self):
        return  f"房子的剩余面积{self.spacearea}房子内的家居{self.jiaju}"

if __name__ == '__main__':
    zhuozi = Furniture("桌子", 10)
    chuang = Furniture("床", 8)
    hjc = Room()
    hjc.add(zhuozi)
    hjc.add(chuang)
    print(hjc)







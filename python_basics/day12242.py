#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/24 20:30

import os

# os.rename("D:/work--learn/python_study/readme", "D:/work--learn/python_study/readme.txt")
# os.remove("D:/work--learn/python_study/readme[备份].txt")

# os.mkdir("studypython")
# os.rmdir("studypython")
os.chdir("D:/work--learn/python_study")

path = os.getcwd()
print(path)

data = os.listdir()
print(data)
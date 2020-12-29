#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/24 18:15

with open("D:/work--learn/python_study/readme.txt","r", encoding="utf-8") as f:
    # f.write("我撑把完整的\njinzidasui")
    f.seek(6, 0)
    data = f.read()
    # data.encode("utf-8")
    print(data)


with open("D:/work--learn/python_study/image/0.jpg", "rb") as f:
    data = f.read()

print(data)

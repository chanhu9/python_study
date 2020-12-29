#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/24 20:08

dataname = input("请输入要备份的文件名")
index = dataname.find(".")
name_list = dataname.split(".")
print(index)
print(name_list)
newname2 = dataname[:index] + "[备份]" + dataname[index:]
newname = name_list[0] + "[备份]" + "." + name_list[1]
print(newname)
print(newname2)

h = open("D:/work--learn/python_study/" + newname, "a")

with open("D:/work--learn/python_study/" + dataname, "r") as f:
    while True:
        data = f.readline(1024)
        if len(data) == 0:
            h.close()
            break
        else:
            # with open("D:/work--learn/python_study/" + newname, "a") as h:
                h.write(data)

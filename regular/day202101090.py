#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/9 10:37

import re

data = "chanhu9@126.com"
data2 = ["apple", "banana", "orange", "pear", "watermelon"]

data3 = "qq:5454561"

#
# for value in data2:
#
#     res = re.match("apple|banana", value)
#     try:
#         res2 = res.group()
#         print(res2)
#     except :
#         print("没有匹配到 ")

# res = re.match("^\w[0-9]{1,8}|.*9@126\.com$", data)

# res = re.match("[a-z0-9]{1,16}@(qq|126|sina|163).com", data)

data4 = "<html>hh</html>"

data5 = "<html><h1>www.itcast.cn</h1></html>"

data6 = "18/188/"

# res = re.match("<([a-zA-Z1-6]+)>.*</\\1>", data4)

res = re.match(r"^(\d+)/(\d+)/$", data6)

res2 = res.group()
print(res2)
#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 14:11

import json

data_list = [{"name":"guanyu"}, {"age":18}, {"sex":"男"}]

data_json = json.dumps(data_list, ensure_ascii=False)
print(type(data_json))
print(data_json)

for i in data_list:
    print(i)
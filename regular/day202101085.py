#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 19:42

import copy

my_name = "hjc"
my_list = ["hjc", 18, [1,2], (1,2)]
my_tup = ("abc", 18, [1,2])

my_dict = {"name":"hjc", "age":18, "friend":["guanyu","zhangfei","liubei"]}

my_tup2 = copy.copy(my_tup)
my_tup3 = copy.deepcopy(my_tup)
print(id(my_tup))
print(id(my_tup2))
print(id(my_tup3))
print("====================")
print(id(my_tup[0]))
print(id(my_tup[1]))
print(id(my_tup[2]))

print("====================")
print(id(my_tup2[0]))
print(id(my_tup2[1]))
print(id(my_tup2[2]))
print("====================")
print(id(my_tup3[0]))
print(id(my_tup3[1]))
print(id(my_tup3[2]))




#
# my_name2 = copy.copy(my_name)
# print(id(my_name))
# print(id(my_name2))
#
# my_list2 = copy.copy(my_list)
# my_list3 = copy.deepcopy(my_list)

# print(id(my_list))
# print(id(my_list[0]))
# print(id(my_list[1]))
# print(id(my_list[2]))
# # print(id(my_list[2][0]))
# print(id(my_list[3]))
# print("==========================")
# print(id(my_list2))
# print(id(my_list2[0]))
# print(id(my_list2[1]))
# print(id(my_list2[2]))
# print(id(my_list2[3]))
# print("==========================")
# # print(id(my_list3))
# print(id(my_list3[0]))
# print(id(my_list3[1]))
# print(id(my_list3[2]))
# print(id(my_list3[2][0]))
# print(id(my_list3[3]))
#
#

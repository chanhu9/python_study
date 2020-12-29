#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/23 19:18

print("hello %s"%2, end="---")
print(type(eval("3 + 2")))

def compare(a,b):
    "这是一个比较函数"
    a = a if a > b else b
    print(a)

compare(1,3)

print(len("ertyui tyuio"))

list1 = [1,2,3,4,5,6]
print(max(list1))
print(min(list1))

for i in range(3):
    print(i, end="")


for i in enumerate(list1):
    print(i,end="a")

list2 = ["asas","saa","ad3wew","erw","dsfwd","acdc","sda","dfe","dsfs","aaa"]

my_list = [i for i in list2 if "a" not in i]
print(my_list)

print("===================")
my_list2 = [{cell:cell.index(i)} for cell in list2 for i in cell if i == "a" ]
print(my_list2)
list3 = ["a","s","d"]
list4 = ["1","2","3"]

mydict1 = [{list3[i]:list4[i]} for i in range(len(list3))]
print(mydict1)

mydict2 = {"name1":85,"name2":45,"name3":55,"name4":65,"name5":7,"name6":683,"name7":74,"name8":65,"name9":95}

res = [{k:v}for k,v in mydict2.items() if v > 80]
print(res)


help(compare)

def fun1(*args):
    print(args)

fun1(1,2,3,"as")


def fun2(**kwargs):
    print(kwargs)

fun2(a=3, b=4, n=5)


def sun(n):
    if n == 0:
        return 1
    res = n + sun(n-1)

    return res

res = sun(3)
print(res)

fun3 = lambda a,b :a if a > b else b
print(fun3(5,4))


fun4 = lambda a=100:a
print(fun4())
print(fun4)

fun5 = lambda **kwargs:kwargs
print(fun5(b=2, a=3))

mylist3 = [{"name":85},{"name":45},{"name":55},{"name":65},{"name":7},{"name":83},{"name":74},{"name":65},{"name":95}]
mylist3.sort(key = lambda data:data["name"], reverse=True)
print(mylist3)


print(abs(-3),abs(4))
print(round(6.45))


def fun6(a, b, f):

    return f(a) + f(b)

res3 = fun6(3.33, 5.67, round)
print(res3)



res4 = fun6(-3, 5, abs)
print(res4)

import functools
list4 = [3, 5, 6, 9]

def fun7(data):

    return 3 * data

res5 = map(fun7, list4)
print(list(res5))
print(type(res5))

def fun8(a, b):

    return a + b

res6 = functools.reduce(fun8, list4)
print(res6)

def fun9(a):

    return a % 2 == 0

res7 = filter(fun9, list4)
print(res7)
print(list(res7))
print(type(res7))
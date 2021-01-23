#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 18:44

my_list = [i for i in range(5)]
print(my_list)

my_genero = (i for i in range(5))
print(my_genero)

for i in my_genero:
    print(i)
# print(my_genero.__next__())
#
# print(next(my_genero))


def fun1():
    # print("=========")
    for i in range(5):
        print("begin")
        yield i
        # print(i)
        print("end")


for i in fun1():
    print(i)

# m = fun1()
# next(m)
# next(m)
# next(m)


def fibonacci(num):
    a = 0
    b = 1
    sum = 0

    while sum <= num:
        result = a
        a, b = b, a + b

        sum += 1
        yield result
        print(a)

gen = fibonacci(10)
print(gen)
for i in gen:
    print("=====")

#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/6 20:32

class MyDecorate:

    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args, **kwargs):
        print("执行前置条件")
        self.fun(*args, **kwargs)
        print("执行后置条件")


@MyDecorate
def fun2(name, age):
    print(f"{name}{age}")

fun2("关羽",18)
#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/6 20:20



def make(name):
    def check(fun):
        if name == "关羽":
            def inner(*args, **kwargs):
                print("执行前置")
                res = fun(*args, **kwargs)

                return res
            return inner

        else:
            def inner(*args, **kwargs):
                res = fun(*args, **kwargs)
                print("执行后置")

                return res
            return inner

    return check

@make("张飞")
def fun():
    print("hello world")

fun()
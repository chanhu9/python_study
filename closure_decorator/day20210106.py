#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/6 19:04

def fun1(name):

    def fun2(content):

        print(f"{name}:{content}")


    return fun2


guanyu = fun1("关羽")
zhangfei= fun1("张飞")

guanyu("三弟，我找的你好辛苦啊")
zhangfei("想死我了")
guanyu("想你妹")


def fun_out(a):

    def fun_inner(b):
        nonlocal a
        a = 10
        print(a + b)

    print(a)
    fun_inner(2)
    print(a)

    return fun_inner


res = fun_out(1)
print(res(2))




def check(fun):
    def inner(name):
        print("请先下载注册")
        fun(name)

        return "ok"
    return inner

# fun = check(fun)
# res = fun("关羽")
# print(res)

@check
def fun(name):
    print(f"{name}要使用小巴生活")

res = fun("刘备")
print(res)
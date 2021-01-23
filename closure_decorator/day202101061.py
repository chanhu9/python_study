#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/6 19:45
import time


def check(fun):

    def inner(*args, **kwargs):
        begin_time = time.time()
        res = fun(*args, **kwargs)
        end_time = time.time()
        print(f"开始时间：{begin_time}结束花时间：{end_time}")

        return res
    return inner

@check
def fun():
    sum = 0
    print(sum)

fun()


def make_div(fun):
    def inner():
        print("=====<div>======")
        fun()

    return inner

def make_p(fun):
    def inner():
        print("=====<p>======")
        fun()

    return inner
@make_p
@make_div
def fun():
    print("hello world")

fun()
#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/7 16:46

import os
import time
print(os.getcwd())
print(os.chdir(r"D:\work--learn\python_study"))

def rount(request_path):

    def decorate(func):
        rount_list.append((request_path, func))

        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return inner
    return decorate


@rount("/index.html")
def index():
    '响应码'
    status = "200 OK"

    "响应头"
    response_headers = [("Connection", "keep-alive"), ("Content-Type", "application/json"), ("Transfer-Encoding", "chunked")]

    with open("./template/index.html", "r", encoding="utf-8") as f:
        filedata = f.read()

    timedata = time.ctime()
    print(timedata)

    res = filedata.replace("{%content%}", timedata)

    return status, response_headers, res


@rount("/center.html")
def center():
    status = "200 OK"

    response_headers = [("Connection", "keep-alive"), ("Content-Type", "application/json")]

    with open("./template/center.html", "r", encoding="utf-8") as f:
        file_data = f.read()

    time_data = time.ctime()

    res = file_data.replace("{%content%}", time_data)

    return status, response_headers, res


def error():
    status = "404 not found"

    response_headers = [("Connection", "keep-alive"), ("Content-Type", "application/json")]

    res = "not found"

    return status, response_headers, res


# path = {"request_path":"/index.html"}
def handle_request(request_path):

    path = request_path["request_path"]

    if path == "/index.html":
        res = index()

        return res


    elif path == "/center.html":
        res = center()

        return res

    else:
        res = error()

        return res

rount_list = [("/index.html",index),("/center.html",center)]


def handle_request2(request_path):

    for path ,func in rount_list:
        if request_path == path:
            res = func()
            return res

        else:
            res = error()

            return res



if __name__ == '__main__':
    pass
    # handle_request(path)

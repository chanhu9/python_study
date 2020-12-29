#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2020/12/29 9:55
import time

class LllegalPassword(Exception):

    def __init__(self, length):
        self.length = length


    def __str__(self):
        return f"你输入的密码长度是{self.length}，密码长度为6到20位的数字和字母组合"

try:
    f = open(r"D:\work--learn\python_study\readme.txt", "r", encoding="utf-8")
    try:
        while True:
            data = f.readline()
            if len(data) < 6:
                raise LllegalPassword(len(data))
            else:
                # time.sleep(2)
                print(data)
    except Exception as e:
        print(e)
        print("因为意外，读取文件终止")
        f.close()
except:
    print("文件不存在")





if __name__ == '__main__':
    pass
    # try:
    #     password = input("请输入你的密码")
    #     length = len(password)
    #     if length < 6 or length > 20:
    #         raise LllegalPassword(length)
    # except Exception as resule:
    #     print(resule)
    #
    # else:
    #     print("密码设置成功")

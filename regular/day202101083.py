#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 17:25
import pymysql

from contextlib import contextmanager

@contextmanager
def connect():
    db = pymysql.connect(host="rm-bp130dahx82uk26a0.mysql.rds.aliyuncs.com", port=3306, user="local_user",
                              passwd="dev123456!", charset="utf8")

    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    print("和数据库建立链接")

    yield cursor

    print("关闭数据库链接")
    cursor.close()
    db.close()




sql = "select * from member.life_member where id=6;"

with connect() as mydb:
    mydb.execute(sql)
    res = mydb.fetchone()
print(res)




#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 16:46

import pymysql


class MyDb:

    def __init__(self, environment):
        self.dbname = environment

    def __enter__(self):
        if self.dbname == "dev":
            self.db = pymysql.connect(host="rm-bp130dahx82uk26a0.mysql.rds.aliyuncs.com", port=3306, user="local_user",
                            passwd="dev123456!", charset="utf8")

            self.cursor = self.db.cursor(cursor=None)
            print("和数据库建立链接")

            return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("断开链接")

        self.cursor.close()
        self.db.close()


    def select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()

        return res

if __name__ == '__main__':
    sql = "select * from member.life_member where id=6;"

    with MyDb("dev") as mydb:
        data = mydb.select(sql)
    print(data)
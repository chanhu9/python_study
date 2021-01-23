#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 14:36

import logging

logging.basicConfig(filename="log.txt",
                    format="%(asctime)s--%(filename)s--[line:%(lineno)d]--%(levelname)s--%(message)s",
                    level=logging.DEBUG,
                    filemode="a")

logging.info("这个傻狗I一个")
logging.debug("这个是一个傻狗")
logging.warning("哈哈哈杀掉一个")
logging.error("我说的是沙雕")
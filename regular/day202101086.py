#!/usr/bin/env python3
# encoding: utf-8
#@author : hujincheng
#@time : 2021/1/8 20:13

import re

# data = "Rn5 ty8ihj好*&%$!2hgfdsfghj"

# res = re.match("Rn5\sty\di\D\S\w\W", data)

# data = "565aaaddddat2020weekmy0108decorate2048"


# res = re.match("a*dat", data)
# res = re.match("a+dat", data)
# res = re.match("a?dat", data)
# res = re.match("a{3}dat", data)
# res = re.match(".*a{3}dat.*", data)
# res = re.match("\d+a?[d]*", data)
# res = re.match("\d+[a]{3}d{2,4}", data)

"""
^ : 开头
$ : 结尾
"""
# data = "2132AYH1rtyuioy@qq.com"
# data = "15566668888"

# res = re.match("^\d.*[4r]$", data)
# res = re.match("^\d[a-zA-Z0-9]{6,20}[@]\w+(.com)$", data)
# res = re.match("^[1][0-9]{9}\d$", data)


data = "52659854@qq.com"
res = re.match("", data)


res2 = res.group()
print(res2)


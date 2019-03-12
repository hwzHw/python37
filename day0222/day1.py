#
# @Time    : 2019/2/22 15:34
# @Author  : Mat
# @壮      ：Very Cool
# @File    : day1.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................
"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/11/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import requests
import json
import pymysql
import re
import math
import time
import random


# conn = pymysql.connect(host='127.0.0.1',port=3306,users='root',password='123456',db='dbstock',charset='utf8')
# cur = conn.cursor()
count_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount'
data_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'

type_list = ["sh_a","sh_b","sz_a","sz_b","sh_z","sz_z"]
page = 1
size = 40
#type = "sh_b"
pat1 = re.compile(r'"(\d+)"')
pat2 = re.compile(r'\{(.+?)\}')
headers = {'User-Agent':'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}


for type in type_list:
    param1 = {
        "node":type
    }
    html = requests.get(url=count_url,params=param1,headers=headers).text
    count = int(pat1.search(html).group(1))
    page_count =  math.ceil((count / size))
    print(count,page_count)
    for page in range(1,page_count+1):
        param2 = {
            "page": page,
            "num": size,
            "sort": "symbol",
            "asc": 1,
            "node": type,
            "_s_r_a": "init"
        }
        print('type:',type,' page:',page)
        html = requests.get(url=data_url,params=param2,headers=headers).text
        #print(html)
        ls = pat2.findall(html)
        #print(len(ls))
        for item in ls:
            print(item)
            tmps = item.split(',')
            values = []
            for tmp in tmps:
                tmps2 = tmp.split(':')
                key = tmps2[0]
                value = tmps2[1].replace('"','')
                values.append(value)
                #print(key,value)
            for i in range(3,12):
                values[i] = float(values[i])
            for i in range(12,14):
                values[i] = int(values[i])
            for i in range(15, 20):
                values[i] = float(values[i])

            values.append(type)
            #print(values)
            print('='*36)
            strSql = 'insert into tbstock VALUES(0,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # cur.execute(strSql,values)
            # conn.commit()
        #data = json.loads(html)
        #print(data)
        time.sleep(random.random())

# conn.close()

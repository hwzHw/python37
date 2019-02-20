"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/24'
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
'''
向笑话集插入记录
'''
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',db='dbxhj1809',charset='utf8')
cursor = conn.cursor()
sql = 'insert into xhjtest_xhjinfo VALUES(0,"非常好笑的笑话2","http://www.jokeji.com/sdffds","哈哈哈哈...","2017-12-12",166666)'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()

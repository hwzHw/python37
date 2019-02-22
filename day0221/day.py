#
# @Time    : 2019/2/21 9:44
# @Author  : Mat
# @壮      ：Very Cool
# @File    : day.py
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
# 冒泡排序
# items = [10,30,67,5,18,0,24]
# print(items)
# def sort(items):
#     count = len(items)
#     for i in range(1, count):
#         for j in range(i+1,count):
#             if items[i] > items[j]:
#                 items[i],items[j] = items[i], items[j]
#         print(items)
# sort(items)
# 正则去重
# import re
# a = 'not 404 found 张三 99 深圳'
# list = a.split(' ')
# print(list)
# res = re.findall('\d+|[a-zA-Z]+',a) #数字 | 单词
# for i in res:
#     if i in list:
#         list.remove(i)
# new_str=' '.join(list)
# print(res)
# print(new_str)
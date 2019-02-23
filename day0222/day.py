#
# @Time    : 2019/2/22 10:36
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
import re
# " . " 不可以匹配换行符，匹配任意一个字符（除了\n）
# result = re.findall('.', 'hello \n china', flags=re.M)
# print(result)


# " [] " 匹配[]中列举的字符
# result = re.findall('[01234].ello', '0hello 1hello 2 ello 88ello')
# print(result)


# " \d "  匹配数字 0-9
# result = re.findall('\dhello', 'hello 1hello 5hello 0 hello')
# print(result)


# " \D " 匹配非数字，即不是数字
result = re.findall("\Dhello", "xhello 1hello 5hello 0hello")
print(result)

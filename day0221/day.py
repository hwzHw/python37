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
import socket
from threading import Thread

def readThread():
    BUFFERSIZE = 1024
    while True:
        try:
            databytes = clientSocket.recv(BUFFERSIZE)
            if len(databytes) == 0:
                clientSocket.close()
                break
            else:
                datastr = databytes.decode("gbk")
                print("收到消息", datastr)
        except Exception as e:
            print(e)
            break

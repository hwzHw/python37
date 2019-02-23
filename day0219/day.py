#
# @Time    : 2019/2/19 14:26
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
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
import threading,time


# def fun():
#     time.sleep(1)
#     print('Hello')
#
#
# t = threading.Thread(target=fun)
# t.start()
#
# while True:
#     leng = len(threading.enumerate())
#     print('num%d' % leng)
#     time.sleep(0.2)

# class MyThread(threading.Thread):
#     def __init__(self,arg):
#         super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
#         self.arg=arg
#
#     def run(self):#定义每个线程要运行的函数
#         time.sleep(1)
#         print('the arg is:%s\r' % self.arg)
#
#
# for i in range(4):
#     t =MyThread(i)
#     t.start()
#
# print('main thread end!')
# 锁  好处 确保了 某关键代码只能由一个线程从头到尾的完整的执行
# 坏处  阻止了多线程并发执行
# num = 0
#
#
# def fun1():
#     global num
#     for r in range(100000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#
#
# def fun2():
#     global num
#     for r in range(100000):
#         mutex.acquire()
#         num += 1
#         mutex.release()
#
#
# mutex = threading.Lock()
# t1 = threading.Thread(target=fun1)
# t1.start()
# t2 = threading.Thread(target=fun2)
# t2.start()
# time.sleep(2)
# print(num)


# 多进程修改全局变量    在多进程中每个进程都复制父进程的所有数据，互不影响
# import os
# pid = os.fork()
# num = 1
# print('Hello', num)
# if pid == 0:
#     num += 1
#     print(num)
# else:
#     num += 1
#     print(num)



#
# @Time    : 2019/2/22 16:07
# @Author  : Mat
# @壮      ：Very Cool
# @File    : day2.py
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
# 类属性不会因为实例不同而不同  实例属性通常需要类__init__方法初始化
# 实例可以调类属性，类不可以调用实例属性
# class Doc(object):
#     isAlife = True
#     def __init__(self, _mp):
#         self.mp = _mp
# a1 = Doc(20)
# print(a1.mp)#
# print(a1.isAlife)#实例可以调用类属性

# 类方法 静态方法 实例方法
#实例方法可以调用实例属性 类方法可以访问类的内容
#静态方法不可以访问类内容和实例内容

# 类与对象的区别  类是对象的模板，是对象的抽象化
# 对象=属性+方法（行为）  属性：比如一个动物是什么样的  行为：这个动物所做的动作
#本质区别： 类不代表具体事物，而对象可以
# class Doc(object):
#     def __init__(self, _spead):#构造函数
#         self.spead = _spead#类属性
#     #声明实例方法
#     def run(self):
#         print(self.spead)
#
#     #声明静态方法
#     @staticmethod
#     def dead():
#         print('Hello')
#
#     #声明类方法
#     @classmethod
#     def fun(cls):
#         print('Word')
# a1 = Doc(20)#实例
# a1.run()#实例可以调用实例方法
# a1.dead()#实例可以调用静态方法
# a1.fun()#实例可以调用类方法
# Doc.fun()#类可以调用类方法


#为什么要使用类属性 类方法
#为了减少多个类实例所产生的内存空间
#类方法与类属性属于类，而不属于某个实例

#python是动态语言   是在运行时可以改变其结构的语言
#运行中的函数，对象，甚至代码可以被引进，已有的函数可以被删除或是其它结构上的变化
#动态的添加类属性
# class Doc(object):
#     def __init__(self, _mp):
#         self.mp = _mp#类属性
# a1 = Doc(50)#实例
# print(a1.mp)#实例调用类属性
# Doc.isAlife = True#类可以动态添加类属性
# print(Doc.isAlife)
# print(a1.isAlife)#添加类属性后，实例也拥有了此方法


# 动态添加实例属性
# class Doc(object):
#     def __init__(self,_mp):
#         self.mp = _mp#类属性
# a1 = Doc(20)#实例
# print(a1.mp)
# a1.hp = 50#实例动态添加实例属性
# print(a1.hp)

#可以通过__slots__限制添加的属性
# class Doc(object):
#     __slots__ = ('mp')
#
# a1 = Doc()#实例
# a1.mp = 20
# print(a1.mp)
# Doc.hp = 50#类还是动态的添加属性，实例则不可以
# print(Doc.hp)


# 生成器  iterable  一边计算一边循环的机制
#方法1 列表生成式
# l = [x*x for x in range(5)]
# g = (x*x for x in range(5))
# print(l, type(l))
# print(g, type(g))
# print(next(g))
# for r in g:#可以使用for循环对生成器遍历
#     print(r)

#方法2  用函数来创建 用到关键字yield

# def fib(times):
#     n = 0
#     a, b = 0, 1
#     yield a
#     yield b
#     while n<times:
#         a, b = b, b+a
#         yield b
#         n += 1
#     return 'Hello'
# r = fib(5)#r为生成器对象
# print(r)

#获取函数返回值需要捕获异常
# def fib(times):
#     n = 0
#     a, b = 0, 1
#     yield a
#     yield b
#     while n<times:
# # 0 1 1 2 3 5 8
#         a, b = b, b+a
#         yield b
#         n += 1
#     return "finish"
# r = fib(5)
# print(r)
# while True:
#     try:
#         x = next(r)
#         print(x)
#     except StopIteration as e:
#         print(e.value)
#         break

#生成器的特点   节约内存
#迭代到下一次的调用时，所使用的参数都是第一次所保留的



#可迭代 迭代器
#   可迭代对象
#可以直接作用于for循环的对象统称为可迭代对象，集合数据类型（list,dict,set,str等） iterable
#一类是generator，包括生成器和带yield的

#判断是否可以迭代   可以使用isinstance（）
from collections.abc import Iterator,Iterable
# d = isinstance([], Iterable)
# print(d)

#迭代器 iterator  可以被next（）函数调用并不断返回下一个值的对象
# a = isinstance((x for x in range(5)), Iterator)
# print(a)

# 闭包   闭包必须是一个内嵌函数，内嵌函数调用外部函数的变量，外部函数的返回值是一个内嵌函数
# def func1(a):
#     def func2(b):
#         return a+b
#     return func2
# f1 = func1(100)
# f2 = func1(50)
# print(f2(1))

# 装饰器  在不改变原函数的情况下为函数增加新的功能,由闭包函数和语法糖组成
# 装饰器使用场景  引入日志 函数执行时间统计  权限校验  缓存
# 使用装饰器编写一个时间消耗
# import time
# def fun(times):
#     start = time.time()
#     def func():
#         times()
#         end = time.time()
#         print(end - start)
#     return func
# @fun
# def sart():
#     print('run')
#     time.sleep(1)
# while True:
#     sart()

#复制  浅拷贝 深拷贝
# 复制  传递对象的引用 直接赋值，原队列发生改变，复制后的队列做相同改变
import copy
# l = [1, 2, 3, [4, 5]]
# l2 = l
# l.append(6)
# l[3].append(5.5)
# print(l, id(l))
# print(l2, id(l2))

# 浅拷贝  改变原始队列，浅拷贝后的队列不变，对于内层队列来说，值会做相同改变
# l = [1, 2, 3, [4, 5]]
# l2 = copy.copy(l)
# l.append(6)
# l[3].append(4.5)
# print(l, id(l))
# print(l2, id(l2))

# 深拷贝 拷贝原始队列的值，原队列改变，深拷贝后的队列值不变
#改变原始队列，深拷贝后队列仍然是原始队列的值
# l = [1, 2, 3, [4, 5]]
# l2 = copy.deepcopy(l)
# l.append(6)
# l[3].append(4.5)
# print(l, id(l))
# print(l2, id(l2))

# 元类  元类就是用来创建类的东西  用关键字type可以动态创建类
# 使用元类的好处  拦截类的创建  修改类  返回修改之后的类


# 垃圾回收
# 引用计数来跟踪垃圾回收，通过标记清除来解决循环引用的问题，通过分代回收提高垃圾回收效率
# 什么情况下引用计数+1  对象被创建时，被copy引用，作为参数，作为子元素存储到容器中
# 引用计数-1  对象别名被销毁，引用被赋值新的对象，一个函数离开他的作用域，从容器中删除
# 引用计数优点： 简单 直观，实时性，只要没有了引用就释放资源
# 缺点：维护引用计数需消耗一定的资源，循环应用时无法回收，也正是因为如此才需要标记清除


# python中的单例模式
# 是一种常用的软件设计模式，主要目的是确保某一个类只有一个实例存在，
# 必须自己创建这个实例，必须自行向整个系统提供这个实例
# 可以通过模块来实现，使用__new__，使用装饰器

# 进程线程对比
# 根本区别：进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位
# 每个进程都有独立的代码和数据空间，同一类线程共享代码和数据空间
# 在操作系统中能同时运行多个进程
# 没有线程的进程可以看做是单线程的，如果一个进程内有多个线程，则执行过程不是一条线的，而是多条线（线程）共同完成的
# 线程和进程在使用上各有优缺点：线程执行开销小，但不利于资源的管理和保护，而进程正相反。

# 编写完的代码在没有运行的时候称为程序，正在运行的代码称为进程
# 父子进程的执行顺序没有先后顺序，在多线程中每个进程都赋值父进程的所有数据，互不影响
from multiprocessing import Process
import os, time


def fun(name, age, **kwargs):
    print(name, age, kwargs)
    time.sleep(1)
    print(name, age, kwargs)
    time.sleep(1)
    print(name, age, kwargs)
    time.sleep(1)
    print(name, age, kwargs)


if __name__ == '__main__':
    print('parent pid %d' % os.getpid())
    p = Process(name='chile', target=fun, args=('hwz', 20), kwargs={'Hello': False})
    p.start()
    print('p name %s pid %d' % (p.name, int(p.pid)))
    time.sleep(2)
    p.terminate()
    p.join()
    print('Finish')
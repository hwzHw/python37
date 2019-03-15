#
# @Time    : 2019/3/12 9:19
# @Author  : Mat
# @壮      ：Very Cool
# @File    : ll.py
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
# 进程线程对比
# 进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位
# 每个进程都有独立的代码和数据空间  同一类线程共享代码和数据空间
# 在操作系统中能同时运行多个进程（程序）；而在同一个进程（程序）中有多个线程同时执行
# 内存分配方面：系统在运行的时候会为每个进程分配不同的内存空间；而对线程而言，除了CPU外，系统不会为线程
# 分配内存（线程所使用的资源来自其所属进程的资源），线程组之间只能共享资源
# 包含关系：没有线程的进程可以看做是单线程的，如果一个进程内有多个线程，则执行过程不是一条线的，而是多条
# 线（线程）共同完成的

# 优缺点：线程执行开销小，但不利于资源的管理和保护，而进程正好相反

# 当需要创建得子进程数量不多时，可以直接用multiprocessing中的Process动态生成多个进程
# 但如果目标太多，手动去创建进程的工作量就大，此时就可以用到multiprocessing模块提供的Pool方法
# 初始化进程池时需要给定最大进程数，当请求Pool时会根据当前池子中获取进程，如果有可用进程则执行，如果没有可用
# 进程则等待，直到有可用进程
# 引入系统模块
from django.shortcuts import render, redirect, reverse
# 引入utils模块
from . import utils
from io import BytesIO
# 引入日志模块
import logging
# 引入模块，用于返回json字符串，和http
from django.http import HttpResponse, JsonResponse
# 引入自带系统用户表
from django.contrib.auth.models import User

# 引入系统自带装饰器authenticate,login
from django.contrib.auth import authenticate, login, logout # 引入商品种类表
from django.contrib.auth.decorators import login_required
from . import models
from goods.models import GoodsType, Goods


# 修改用户信息
@login_required
def update(req):
    user = models.User.objects.all()
#     遍历用户信息数据
    for a in user:
        user = models.User.objects.get(pk=a.user_id)
#         判断是否为当前用户
        if user.username == req.session['loginUser']:
            user1 = models.UserInfo.objects.filter()
#             遍历当前用户数据
            for i in user1:
                if req.method == 'GET':
                    return render(req, 'blog/update.html')
                else:
                    # 修改昵称
                    i.nickname = req.POST.get('nackname')
                    # 修改年龄
                    i.age = req.POST.get('age')
                    # 修改邮箱
                    i.email = req.POST.get('email', False)
                    # 保存设置
                    i.save()
                    return redirect(reverse('user:update'))



from django.shortcuts import render,redirect
from django.http import HttpResponse

from user.models import Users  #配置URL 根据 views.py 中 Uses 函数解析
# Create your views here.
from . import models
from django.template import loader


def index(req):
    # print(req.GET["name"])
    # print(HttpResponse)
    # print(dir(HttpResponse))
    return HttpResponse("<h1>用户管理页面</h1>")


# 删
def delete(request):
    Users.usermanager.get(id=8).delete()#单条删除
    # Users.usermanager.all().delete()#全部删除
    # Users.usermanager.filter(id=1 and 5).delete();   #删除多条中间使用and连接
    return HttpResponse('删除数据成功!')


# 改
def update1(request):
    obj = Users.usermanager.get(id=5)   #根据表中的id来修改内容既name
    obj.name = "xiaoli"
    obj.save()
    return HttpResponse('更新数据成功!')


# 2.方法   增加
def create(req):
    # users = models.Users.usermanager.create_user(name='xxx', age=50)
    # return HttpResponse('注册成功')
    return redirect('users:list')

# 1.方法
# def create(requester):
#     users = models.Users().create_user("zhang", 20)
#     users.save()
#     return HttpResponse("注册成功")


# 3.方法
# def create(requester):
#     users = models.Users(name="li", age=22)
#     users.save()
#     users = models.Users(name="wang", age=18)
#     users.save()
#     users = models.Users(name="huang", age=29)
#     users.save()
#     return HttpResponse("注册成功")

# 位置参数方法1
def param1(request,name):
    return HttpResponse("这是一个位置参数1")


# 位置参数方法2
def param2(request,username):
    return HttpResponse("关键字参数2")


def index1(req):
    temp = loader.get_template('users/indexes.html')
    msg = {'name': '娃哈哈'}
    return HttpResponse(temp.render(msg, req))


def index2(req):
    msg = {'name': '登录'}
    user = models.Users.usermanager.get(id=13)
    users = models.Users.usermanager.all()

    # return HttpResponse(render(req, 'indexes.html', {"users": users, "users": users}))

    # 继承
    return HttpResponse(render(req, 'base.html', {"users": user, "users": users}))


def index3(req):
    return render(req, "indexes.html")


#用来继承页面的方法
def update(req):
    return render(req, 'users/update.html')


def list(req):
    # users = models.Users.usermanager.all()
    # return HttpResponse(render(req, 'base.html', {"users": users, "users": users}))
    if req.method == 'GET':
        return render(req, 'users/list.html')
    elif req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        print('name,age')
        return redirect('users:list')

from django.shortcuts import render

from django.http import HttpResponse
from . import models
from django.shortcuts import render,redirect

from django.db import models
from tinymce.models import HTMLField

from . import utils
from io import BytesIO


def index(req):
    # username = 'Hello World'
    # age = 25
    # genger = '女'
    # 数据校验

    # 保存数据
    # 1.调用类方法
    # user = models.User.create_user(username, age, genger)
    # user.save()

    # 2.
    # user = models.User(username=username, age=age, genger=genger)
    # user.save()
    context = {
        "msg": "本是青灯不归客，却因浊酒恋红尘"
    }
    return render(req, 'blog/index.html', context)
    # return HttpResponse('<h1>首页</h1>')


def register(req):
    return render(req, 'blog/register.html')


def login(req):
    if req.method =='GET':
        return render(req, 'blog/login.html')
    elif req.method =='POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        try:
            u = models.User.objacts.get(name=name,age=age)
            return render(req, 'blog/index.html')
        except:
            return render(req, 'blog/login.html')
    # return render(req, 'blog/login.html')


def list(req):
    return HttpResponse('<h1>列表</h1>')


# 定义模型类
class GoodsInfo(models.Model):
    gcontent = HTMLField()


def create_code(request):
    f = BytesIO()
    img, code = utils.creatr_code()
    img.save(f, 'PNG')
    request.session['code'] = code
    return HttpResponse(f.getvalue())


def regist(request):
    # if request.method == 'GET':
    #     return render(request, 'blog/regist.html', {'msg': 'Hello'})
    # elif request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     nickname = request.POST['nickname']
    #     avatar = request.FILES['avatar']
    #     path = 'static/imge' + avatar.name
    #     with open(path, "wb")as file:
    #         for f in avatar.chunks():
    #             file.write(f)
    #     user = models.User(username=username,password=password,nickname=nickname,avatar=path)
    #     user.save()
    #     return render(request,'blog/login.html', {'msg':'成功', 'user':'user'}),
    if request.method == 'GET':
        return render(request, 'blog/regist.html', {'msg': 'Hello'})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']
        avatar = request.FILES['avatar']
        print(avatar)
        user = models.User(username=username, password=password, nickname=nickname)
        user.save()
        return render(request, 'blog/login.html', {'msg':'成功', 'user':'user'}),


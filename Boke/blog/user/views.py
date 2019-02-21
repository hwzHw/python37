from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from . import models
from django.template import loader
from hashlib import md5
# Create your views here.
from . import utils
from . import forms
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# from django.core import serializers
from django.core.serializers import serialize
from django.db import transaction
# 分页
from django.core.paginator import Paginator
from django.conf import settings




def param(requset, name):
    print(name)
    # print(dir(requset))          #显示请求头数据
    # print(requset.path)          #显示路径
    # print(requset.method)        #显示请求方法
    # return HttpResponse("位置参数")
    user = models.Users.objects.get(id=name)
    arts = user.arts.all()
    return render(requset, 'user/listTitle.html', {'user': user, 'arts': arts})


def index(req):
    return render(req, 'user/index.html')


def register(req):
    return render(req, 'user/register.html')


# 判断登录
@csrf_exempt  # 第二种请求安全认证的方法
def login_success(req):
    username = req.POST.get('username', )
    password = req.POST.get('password', )
    # yanzheng = req.POST.get('yanzheng', )
    # code = req.session['code']
    # print(code)

    # md5util = md5()
    # md5util.update(password.encode('utf8'))
    # pwd1 = md5util.hexdigest()

    try:
        user = models.Users.objects.get(name=username, pwd=password)
        arts = user.arts.all()
        req.session['loginUser'] = user
        return redirect("user:user_index")
    except:
        error = '用户名或密码错误'
        return render(req, 'user/index.html', {'error': error})


# 判断注册
@csrf_exempt
def regist_success(req):
    if req.method == 'GET':
        pass
    if req.method == 'POST':
        name = req.POST.get('username')
        pwd = req.POST.get('password')
        sex = req.POST.get('sex')
        data = req.POST.get('data')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        cusID = req.POST.get('cusID')
        header = req.FILES["header"]
        print(sex, name, pwd, data, email, phone, cusID, header)
        if 6 < len(pwd) < 18:
            return HttpResponse('<h1>密码需在6~18位之间，请重新注册！</h1>')

        # md5util = md5()
        # md5util.update(pwd.encode('utf8'))
        # pwd1 = md5util.hexdigest()
        try:
            user = models.Users.objects.get(name=name)
            return HttpResponse('<h1>用户名存在</h1>')
        except:
            models.Users.objects.create(name=name, pwd=pwd, sex=sex, data=data, email=email, phone=phone, cusID=cusID,
                                        header=header)
            return redirect('user:index')


# 所有文章内容
def user_index(req):
    user = req.session['loginUser']
    arts = user.arts.all()

    users = models.Users.objects.all()
    allarts = models.Article.objects.all()

    return render(req, 'user/user_index.html', {'user': user, 'arts': arts, 'allarts': allarts, 'users': users})


# 个人文章
def user_articles(req):
    user = req.session['loginUser']
    arts = user.arts.all()

    pagenum = req.GET.get('pagenum', default=1)
    pagena = Paginator(arts, settings.PAGESIZE)
    page = pagena.page(int(pagenum))
    return render(req, 'user/user_articles.html', {'arts': arts, 'user': user, 'pagena': pagena, 'page': page})


# 退出登录
def quit(req):
    del req.session['loginUser']
    return redirect("user:index")


# 用户列表
def listUsers(req):
    users = models.Users.objects.all()
    return render(req, 'user/listUsers.html', {'users': users})


# 个人资料及修改
def user_detail(req):
    if req.method == 'GET':
        id = req.GET.get('sid')
        user = models.Users.objects.get(id=id)
        return render(req, 'user/user_detail.html', {'user': user})
    elif req.method == 'POST':
        id = req.POST.get('sid')
        name = req.POST.get('username')
        pwd = req.POST.get('password')
        sex = req.POST.get('sex')
        data = req.POST.get('data')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        cusID = req.POST.get('cusID')

        user = models.Users.objects.get(id=id)
        user.name = name
        user.pwd = pwd
        user.sex = sex
        user.data = data
        user.email = email
        user.phone = phone
        user.cusID = cusID
        try:
            header = req.FILES["header"]
            user.header = header
        except:
            pass
        user.save()
        return redirect("user:user_index")


# 别人作者资料
def user_otherDetail(req, id):
    user = models.Users.objects.get(id=id)
    return render(req, 'user/user_otherDetail.html', {'user': user})


# 添加文章
def addArticle(req):
    id = req.session['loginUser'].id
    return render(req, 'user/addArticle.html', {"author": id})


# 判断添加文章
def addArticle_success(req):
    if req.method == 'GET':
        pass
    elif req.method == 'POST':
        author = req.POST.get('sid')
        title = req.POST.get('title')
        content = req.POST.get('content')
    models.Article.objects.create(title=title, content=content, author_id=author)
    return redirect('user:user_articles')


# 修改文章
def updateArticle(req):
    if req.method == 'GET':
        id = req.GET.get('sid')
        art = models.Article.objects.get(id=id)
        return render(req, 'user/updateArticle.html', {'art': art})
    elif req.method == 'POST':
        id = req.POST.get('sid')
        title = req.POST.get('title')
        content = req.POST.get('content')
        art = models.Article.objects.get(id=id)
        art.title = title
        art.content = content
        art.save()
        userid = art.author_id
        return redirect("user:user_articles")


# 删除文章
def delArticle(req, id):
    art = models.Article.objects.get(id=id)
    art.delete()
    return redirect("user:user_articles")


# 验证码
def createCode(req):
    # 准备响应出去的字节流
    f = BytesIO()
    img, code = utils.create_code()
    # 放入回话作用域
    req.session['code'] = code
    # 图片放入流
    img.save(f, 'PNG')
    return HttpResponse(f.getvalue())

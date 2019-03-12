from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    # 不需要使用@classmethod
    # ttu = models.Users(name='PPP', age=12)
    # ttu.save()
    if request.method == 'GET':
        # print('get方式移交')
        # name = request.GET['name']
        # pwd = request.GET['pwd']
        # favs = request.GET['fav']
        # print(name, pwd, favs)
        name = request.GET.get('name','默认值')
        pwd = request.GET.get('pwd')
        favs = request.GET.getlist('fav')
        print(name, pwd, favs)
    elif request.method == 'POST':
        name = request.POST.get('name', '默认值')
        pwd = request.POST.get('pwd')
        favs = request.POST.getlist('fav')
        print(name, pwd, favs)
    return HttpResponse("<h1>博客首页</h1>")


def login(request):
    # 使用@classmetod
    author = models.Users.create(name='Hello World', age=20)
    author.save()
    return HttpResponse("<h1>登录</h1>")


# restful 格式  添加路径参数(位置参数)
def reg(request, good):
    print(good)
    # models.Users.user.create_author('oooo', 23)
    return HttpResponse("<h1>注册</h1>")


def list(request):
    # 第一种 loader方法
    # temp = loader.get_template("myblog/index.html")
    # context = {'msg': '列表'}
    # return HttpResponse(temp.render(context, request))

    # 第二种render
    return render(request, 'myblog/index.html')


def register(request):
    return render(request, 'myblog/register.html')
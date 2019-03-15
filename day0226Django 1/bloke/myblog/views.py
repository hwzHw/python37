from . import models
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect


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


# def login(request):
#     # 使用@classmetod
#     author = models.Users.create(name='Hello World', age=20)
#     author.save()
#     return HttpResponse("<h1>登录</h1>")
# 判断登录
@csrf_exempt  # 第二种请求安全认证的方法
def login(req):
    username = req.POST.get('username', )
    password = req.POST.get('password', )
    yanzheng = req.POST.get('yanzheng')
    code = req.session.get('code')
    if yanzheng != code:
        return render(req, 'user/index.html', {'error': '验证码错误！'})
    try:
        user = models.Users.objects.get(name=username, pwd=password)
        req.session['user_id'] = user.id
        arts = user.arts.all()
        req.session['loginUser'] = user
        return redirect("myblog:index")
    except:
        error = '用户名或密码错误'
        return render(req, 'myblog/index.html', {'error': error})


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


# def register(request):
#     return render(request, 'myblog/register.html')

# 判断注册
@csrf_exempt
def register(req):
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
        try:
            header = req.FILES["header"]
            models.Users.objects.create(name=name, pwd=pwd, sex=sex, data=data, email=email, phone=phone, cusID=cusID,
                                    header=header)
            return redirect('myblog:index')
        except:
            print(sex, name, pwd, data, email, phone, cusID)
            if 12 < len(pwd):
                return HttpResponse('<h1>密码需在0~11位之间，请重新注册！</h1>')
            try:
                user = models.Users.objects.get(name=name)
                user.save()
                return HttpResponse('<h1>用户名存在</h1>')
            except:
                models.Users.objects.create(name=name, pwd=pwd, sex=sex, data=data, email=email, phone=phone, cusID=cusID)
                return redirect('myblog:index')


# Create your views here.

from django.shortcuts import render, redirect, reverse
from . import models
from django.views.decorators.csrf import csrf_exempt
#会话判断登录
from django.contrib.auth.decorators import login_required
#引入系统内置用户管理表
from django.contrib.auth.models import User
#判断用户管理表 装饰器
from django.contrib.auth import authenticate, login, logout


#主页
def index(req):
    return render(req, 'index.html')


#登录以后的主页
def user_index(req):
    user = models.UserInfo.objects.get(user_id=req.user.id)

    return render(req, 'users/index.html', {'users': user})


#登录
def user_login(req):

    return render(req, 'users/login.html', {})


# 判断登录
def login_success(req):
    username = req.POST.get('username', )
    password = req.POST.get('password', )
    # yanzheng = req.POST.get('yanzheng', )
    # code = req.session['code']
    # print(code)

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            #将验证通过的信息保存在req中，获取为req.users
            login(req, user)
            return redirect('users:user_index')
        else:
            error = '帐号被锁定，请联系管理员'
            return render(req, 'users/login.html', {'error': error})
    else:
        error = '用户名或密码错误'
        return render(req, 'users/login.html', {'error': error})


#注册
def user_register(req):
    return render(req, 'users/register.html')


#判断注册
@csrf_exempt
def register_success(req):
    if req.method == 'GET':
        pass
    if req.method == 'POST':
        username = req.POST.get('username')
        pickname = req.POST.get('pickname')
        pwd = req.POST.get('password')
        sex = req.POST.get('sex')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        cusID = req.POST.get('cusID')
        header = req.FILES["header"]
        if 6 < len(pwd) < 18:
            return render(req, 'users/register.html', {'error': '密码不符合规定'})

        try:
            User.objects.get(username=username)
            return render(req, 'users/register.html', {'error': '用户名存在'})
        except:
            user = User.objects.create_user(username=username, password=pwd, email=email)
            models.UserInfo.objects.create(pickname=pickname, gender=sex, phone=phone, cusID=cusID,
                                        header=header, user=user)
            return redirect('users:user_login')


#用户退出
def user_logout(req):
    logout(req)
    return render(req, 'index.html')


#个人资料
@login_required
def user_info(req):
    rootuser = req.user
    user = models.UserInfo.objects.get(user_id=req.user.id)
    return render(req,'users/user_info.html', {'users':user, 'rootuser':rootuser})


#个人资料修改
def user_update(req):
    if req.method == 'GET':
        pass
    if req.method == 'POST':
        pickname = req.POST.get('pickname')
        sex = req.POST.get('sex')
        age = req.POST.get('age')
        phone = req.POST.get('phone')
        header = req.FILES["header"]

        user = models.UserInfo.objects.get(user=req.user)
        user.pickname = pickname
        user.gender = sex
        user.age = age
        user.phone = phone
        user.header = header
        user.save()
        return redirect('users:user_info')


#添加收获地址
def add_address(req):
    if req.method == 'GET':
        return render(req, 'users/add_address.html', {})
    else:
        recv_name = req.POST['recv_name']
        recv_tel = req.POST['recv_tel']
        province = req.POST['province']
        city = req.POST['city']
        area = req.POST['area']
        street = req.POST['street']
        desc = req.POST['desc']

        try:
            req.POST['is_default']
            addresses = models.Address.objects.filter(user=req.user)
            for address in addresses:
                address.is_default = False
                address.save()

            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province,
                           city=city, area=area, street=street, desc=desc, user=req.user, is_default=True)
            address.save()
        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province,
                                     city=city, area=area, street=street, desc=desc, user=req.user, is_default=False)
            address.save()

        return redirect(reverse('users:list_address'))


#查看所有收获地址
def list_address(req):
    addresses = models.Address.objects.filter(user=req.user)

    return render(req, 'users/list_address.html', {'addresses': addresses})


#删除收获地址
def delete_address(req, aid):
    address = models.Address.objects.get(pk=aid)
    address.delete()

    return redirect(reverse('users:list_address'))


#修改收获地址
def update_address(req, aid):
    if req.method == 'GET':
        address = models.Address.objects.get(pk=aid)
        return render(req, 'users/update_address.html', {'address': address})
    else:
        recv_name = req.POST['recv_name']
        recv_tel = req.POST['recv_tel']
        province = req.POST['province']
        city = req.POST['city']
        area = req.POST['area']
        street = req.POST['street']
        desc = req.POST['desc']
        address = models.Address.objects.get(pk=aid)
        try:
            req.POST['is_default']
            address.is_default = True
            address.save()

        except:
            pass
        address.recv_name = recv_name
        address.recv_tel = recv_tel
        address.province = province
        address.city = city
        address.area = area
        address.street = street
        address.desc = desc
        address.save()
        return redirect(reverse('users:list_address'))
















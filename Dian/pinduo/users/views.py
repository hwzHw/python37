from . import models
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
# 引入模块
from .import models
# 引入系统自带装饰器authenticate,login
from django.contrib.auth import authenticate, login, logout # 引入商品种类表
from django.contrib.auth.decorators import login_required

from goods.models import GoodsType, Goods


# 展示首页数据
def index(request):
    """
    展示首页信息，将用户返回到界面上
    :param request:
    :return:
    """
    # 第一个一级类型数据
    good_type1 = GoodsType.objects.filter(pk=10001)
    # 一级类型所对应的二级类型
    good_type1_2 = GoodsType.objects.filter(parent=good_type1)
    # fffff
    goods1_list = Goods.objects.filter(goodstype__in=good_type1_2)
    # print(good_type1_2, good_type1)

    # 第二个一级类型数据
    good_type2 = GoodsType.objects.filter(pk=10002)
    # 一级类型所对应的二级类型
    good_type2_2 = GoodsType.objects.filter(parent=good_type2)
    # fffff
    goods2_list = Goods.objects.filter(goodstype__in=good_type2_2)
    for i in goods2_list:
        print(i)

    # 第三个一级类型数据
    good_type3 = GoodsType.objects.filter(pk=10003)
    # 一级类型所对应的二级类型
    good_type3_2 = GoodsType.objects.filter(parent=good_type3)
    # fffff
    goods3_list = Goods.objects.filter(goodstype__in=good_type3_2)

    # 第四个一级类型数据
    good_type4 = GoodsType.objects.filter(pk=10004)
    # 一级类型所对应的二级类型
    good_type4_2 = GoodsType.objects.filter(parent=good_type4)
    # fffff
    goods4_list = Goods.objects.filter(goodstype__in=good_type4_2)

    # 第五个一级类型数据
    good_type5 = GoodsType.objects.filter(pk=10005)
    # 一级类型所对应的二级类型
    good_type5_2 = GoodsType.objects.filter(parent=good_type5)
    # fffff
    goods5_list = Goods.objects.filter(goodstype__in=good_type5_2)
    # 查询一二级商品数据
    allGoodsType = GoodsType.objects.filter(parent__isnull=True)
    # 返回数据到界面
    return render(request, "blog/index.html", {"allGoodsType": allGoodsType,
                                               "goods1_list": goods1_list,
                                               "goods2_list": goods2_list,
                                               "goods3_list": goods3_list,
                                               "goods4_list": goods4_list,
                                               "goods5_list": goods5_list
                                               })


def user_login(request):
    """
    用户登录
    :param request:
    :return:
    """
    logger = logging.getLogger("django")
    # GET请求
    if request.method == "GET":
        return render(request, "blog/login.html")
    # POST请求
    elif request.method == "POST":
        # 获取用户输入的用户名
        username = request.POST["username1"].strip()
        # 获取用户输入的密码
        password = request.POST["password1"].strip()
        code = request.POST["code"]
        mycode = request.session["code"]
        if code.upper() != mycode.upper():
            return render(request, "blog/login.html", {"msg": "验证码输入错误！"})
        del mycode
        # 验证用户
        user = authenticate(username=username,password=password)
        # 如果用户不为空
        if user is not None:
            # 用户是否锁定
            if user.is_active:
                # 记录当前用户
                request.session['loginUser'] = username
                login(request,user)
                # 用户重定向首页
                return redirect(reverse('users:index'))

            else:
                # 返回用户状态
                return render(request,"blog/login.html",{"msg":"账号已被锁定"})
        # 如果不为空
        else:
            return render(request,"blog/login.html",{"msg":"用户名或密码错误！"})


# 退出用户登录
def del_login(request):
    """
    删除用户信息
    :param request:
    :return:
    """
    # 删除用户缓存
    logout(request)
    # 返回到首页
    return redirect(reverse('users:index'))


# 用户注册
def user_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,"blog/login.html")
    elif request.method == "POST":
        # 获取用户界面数据
        try:
            username = request.POST["username"].strip()
            password = request.POST["password"].strip()
            c_password = request.POST["c_password"].strip()
            print(username,password,c_password,"aaaa")
            code = request.POST["code"]

            mycode = request.session["code"]
            if code.upper() != mycode.upper():
                return render(request, "blog/login.html", {"msg": "验证码输入错误！"})
            del mycode
            # 判断长度
            if len(username) < 1:
                return render(request, "blog/login.html", {"msg": "用户名称不能为空！！"})
            if len(password) < 6:
                return render(request, "blog/login.html", {"msg": "用户密码不能小于六位！！"})
                # return JsonResponse({"msg": "用户密码不能小于六位！！", "success": True})
            if password != c_password:
                return render(request, "blog/login.html", {"msg": "两次密码输入不一致！！"})
            try:
                User.objects.get(username=username)
                return render(request, "blog/login.html", {"msg": "账号已存在，请重新输入！！"})
            except:
                # password = utils.hmac_by_md5(password)
                #保存
                user = User.objects.create_user(username=username,password=password)
                userinfo = models.UserInfo(user=user)
                user.save()
                userinfo.save()

                return render(request, "blog/login.html", {"msg": "账号注册成功,请登录！！"})
        except Exception as e:
            print(e)
            return render(request, "blog/login.html", {"msg": "账号不能为空"})


def check_username(request, username):
    """
    在注册用户时用AJAX检测用户名是否存在
    :param request:
    :param username:
    :return:
    """
    # 检测用户名是否存在
    qs = User.objects.filter(username=username)
    if len(qs):
        return JsonResponse({"msg": "该用户名已存在，请从新输入！！", "success": False})
    else:
        return JsonResponse({"msg": "恭喜您，用户名可用！！", "success": True})


# 验证码
def code(request):
    """
    将验证码返回到界面上，并根据事件刷新验证码
    :param request:
    :return:
    """
    img, code = utils.create_code()
    # 将数据保存到session
    request.session["code"] = code

    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")


@login_required
# 修改用户信息
def update(request):
    """
    修改用户信息
    :param request:
    :return:
    """
    # 查询所有用户信息
    user = models.UserInfo.objects.all()
    # 遍历用户信息数据
    for a in user:
        user = models.User.objects.get(pk=a.user_id)
        #         # 判断用户是否为当前登录用户
        if user.username == request.session['loginUser']:
            # 如果是，传入id，找到用户
            user1 = models.UserInfo.objects.filter(user_id=user.id)
            # 遍历当前用户数据
            for i in user1:
                if request.method == "GET":
                    return render(request, "blog/update.html", {"i": i})
                else:
                    # 修改昵称
                    i.nickname = request.POST.get("nickname")
                    # 修改年龄
                    i.age = request.POST.get("age")
                    # 修改邮箱
                    i.email = request.POST.get("email", False)
                    # 保存设置
                    i.save()
                    return redirect(reverse("users:update"))


@login_required
# 用户修改头像函数
def update_head(request):
    """
    修改用户头像
    :param request:
    :return:
    """
    # 获取用户对象函数
    user = models.UserInfo.objects.all()
    # 便利用户
    for a in user:
        user = models.User.objects.get(pk=a.user_id)
        if user.username == request.session['loginUser']:
            user1 = models.UserInfo.objects.filter(user_id=user.id)
            for i in user1:
                if request.method == "GET":
                    return render(request, "blog/update_head.html", {"i": i})
                else:
                    # 修改头像
                    # i.header = request.FILES.get("head")
                    a = request.FILES.get("head")
                    if a:
                        i.header = a
                        i.save()
                    return redirect(reverse("users:update_head"))


# 用户修改密码函数
def update_password(request,u_id):
    """
    用户修改密码
    :param request:
    :param u_id:
    :return:
    """
    if request.method == "GET":
        return render(request, "blog/update_password.html")
    elif request.method == "POST":
        print(u_id)
        # 获取旧密码
        pwd = request.POST["pwd"]
        # 获取新密码
        n_pwd = request.POST["n_pwd"]
        # 覆盖密码，保存
        c_pwd = request.POST["c_pwd"]
        print(pwd, n_pwd, c_pwd)
        # 判断密码长度
        if len(n_pwd) < 6:
            return render(request, "blog/update_password.html", {"user": request.user.id, "msg": "密码不能小于六位!"})
            # return redirect(reverse("users:update_password", kwargs={"msg":"密码不能小于六位!","u_id":request.user.id}))
        user = authenticate(username=request.user.username,password=pwd)
        if user is not None:
            if n_pwd == c_pwd:
                user.set_password(n_pwd)
                user.save()
                del_login(request)
                return render(request, "blog/login_success.html")
            else:
                return render(request, "blog/update_password.html", {"user": request.user.id, "msg": "两次密码输入不一致"})
        else:
            render(request, "blog/update_password.html", {"user": request.user.id, "msg": "原密码输入错误！"})


# 添加地址
def aaa(request):
    """
    添加用户所住地址
    :param request:
    :return:
    """
    # 获取用户地址对象
    addresses = models.Address.objects.filter(user=request.user)
    if request.method == "GET":
        return render(request, "blog/aaa.html", {"addresses": addresses})
    else:
        # 从前台获取数据
        province = request.POST["province"]
        city = request.POST["city"]
        area = request.POST["area"]
        recv_name = request.POST["recv_name"]
        recv_tel = request.POST["recv_tel"]
        desc = request.POST["desc"]

        try:
            # 说明这个地址设为默认
            request.POST["is_default"]
            # 获取当前用户地址
            addresses = models.Address.objects.filter(user=request.user)
            for address in addresses:
                address.is_default = False
            # 存储
                address.save()
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, \
                           area=area, desc=desc, user=request.user, is_default=True)
            # 存储地址到数据库
            address.save()
        except:
            address = models.Address(recv_name=recv_name, recv_tel=recv_tel, province=province, city=city, \
                            area=area, desc=desc, user=request.user, is_default=False)
            address.save()
        # 重定向到添加地址界面
        return redirect(reverse("users:aaa"))


# 展示用户地址属性
def address_list(request):
    """
    展示用户地址属性
    :param request:
    :return:
    """
    addresses = models.Address.objects.filter(user=request.user)
    return render(request, "blog/aaa.html", {"addresses": addresses})


# 删除用户地址函数
def delete_address(request, id):
    """
    删除用户地址
    :param request:
    :param id:
    :return:
    """
    # user = models.User.objects.get(pk=user_id)
    # user.delete()
    address = models.Address.objects.get(pk=id)
    address.delete()
    return redirect(reverse("users:aaa"))
    # return render(request, "blog/list_address.html", {})


###################################################邮箱注册
from django.conf import settings
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.http import HttpResponse


# 使用邮箱注册账号
def login1(request):
    if request.method == "GET":
        return render(request, "blog/login1.html", {})
    else:
        email = request.POST["username"].strip()
        password = request.POST.get("password").strip()
        try:
            user = models.User.objects.get(username=email)
            return render(request, "blog/login1.html", {"msg": "该用户名称已经存在，请重新填写！！"})
        except:
            # password = utils.hmac_by_md5(password)
            user = User.objects.create_user(username=email, password=password)
            userinfo = models.UserInfo(user=user)
            try:
                user.save()
                userinfo.save()
                try:
                    # 保存成功，发送邮件
                    m_title = "电商账号激活邮件"
                    m_msg = "点击激活您的账号"

                    # 调用JWT来加密和解密需要的数据
                    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
                    code = serializer.dumps({"confirm": user.id}).decode("utf-8")
                    href = "http://127.0.0.1:8000/users/active/" + code + "/"
                    m_html = '<a href="' + href + '" target="_blank">马上点击激活，一个小时内有效</a>'

                    send_mail(m_title, m_msg, settings.EMAIL_FROM, [email], html_message=m_html)
                    return render(request, "blog/login_success.html", {"msg": "恭喜您，注册成功，请登录邮箱激活账号！！"})
                except Exception as t:
                    print(t, 1111111)
                    return render(request, "blog/login1.html", {"msg": "恭喜您，注册成功，邮箱发送失败，请点击重新发送"})

            except Exception as e:
                print(e)
                return render(request, "blog/reg_email.html", {"msg": "注册失败，请重新注册，或者联系管理员"})


def active(request, token):
    """
    激活账号信息
    :param request:
    :param token:
    :return:
    """
    serializer = Serializer(settings.SECRET_KEY, 3600)
    try:
        info = serializer.loads(token)
        print(info)
        active_id = info["confirm"]
        print("需要激活的用户id=={}".format(active_id))

        user = models.User.objects.get(pk=active_id)
        user.is_active = True
        user.save()
        return render(request, "blog/login_success.html", {"msg": "恭喜您，激活账号成功，请登录！！"})
    except Exception as e:
        return HttpResponse("激活失败==>{}".format(e))

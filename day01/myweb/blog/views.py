from django.db import models
from django.views.decorators.csrf import csrf_exempt
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
from django.contrib.auth import authenticate, login


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


def list(req):
    return HttpResponse('<h1>列表</h1>')


# 定义模型类
# class GoodsInfo(models.Model):
#     gcontent = HTMLField()


def create_code(request):
    f = BytesIO()
    img, code = utils.creatr_code()
    img.save(f, 'PNG')
    request.session['code'] = code
    return HttpResponse(f.getvalue())


# 判断注册
@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, "blog/register.html")
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        sex = request.POST.get('sex')
        data = request.POST.get('data')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cusID = request.POST.get('cusID')
        try:
            header = request.FILES["header"]
            models.User.objects.create(name=name, pwd=pwd, sex=sex, data=data, email=email, phone=phone, cusID=cusID,
                                    header=header)
            return redirect('blog:index')
        except:
            print(sex, name, pwd, data, email, phone, cusID)
            if 12 < len(pwd):
                return HttpResponse('<h1>密码需在0~11位之间，请重新注册！</h1>')
            try:
                user = models.User.objects.get(name=name)
                user.save()
                return HttpResponse('<h1>用户名存在</h1>')
            except:
                models.User.objects.create(name=name, pwd=pwd, sex=sex, data=data, email=email, phone=phone, cusID=cusID)
                return redirect('blog:index')


def login_success(request):
    """
    用户登录
    :param request:
    :return:
    """
    logger = logging.getLogger("django")
    # GET请求
    if request.method == "GET":
        return render(request, "blog/login_success.html")
    #     # POST请求
    elif request.method == "POST":
        # 获取用户输入的用户名
        username = request.POST["username"].strip()
        # 获取用户输入的密码
        password = request.POST["password"].strip()
        code = request.POST["code"]
        mycode = request.session["code"]
        if code.upper() != mycode.upper():
            return render(request, "blog/login_success.html", {"msg": "验证码输入错误！"})
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
                return redirect(reverse('blog:index'))

            else:
                # 返回用户状态
                return render(request,"blog/login_success.html",{"msg":"账号已被锁定"})
        # 如果不为空
        else:
            return render(request,"blog/login_success.html",{"msg":"用户名或密码错误！"})


def create_code(request):
    f = BytesIO()
    img, code = utils.creatr_code()
    img.save(f, 'PNG')
    request.session['code'] = code
    return HttpResponse(f.getvalue())










import random
import re

from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
import http.client
import urllib.request
from geetest import GeetestLib  # 极验验证


# 极验验证,请在官网申请ID使用，示例ID不可使用
from apps.users.models import User

# 极验验证的id和key
pc_geetest_id = "9107cbe379daa19cd93b9250f36ba301"  # id
pc_geetest_key = "73dd706e795ba4e67bad328cf6e68970"  # key


# 短信请求的端口
host = "106.ihuyi.com"
# 短信请求的url
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名（例如：cf_demo123）
account = "C61548361"
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "4b6ddd350c0101f18a5356eb61d60ad8"


class RegisterView(View):
    """注册视图"""

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        """
        对注册页面发送过来的form表单数据进行处理
        :return:
        """
        username = ""
        email = ""
        uphone = ""
        user = User.objects.create_user(username, email, password, uphone=uphone)  # type: User
        user.save()
        return render(request, "")


def send_message(request):
    """发送信息的视图函数"""
    # 获取ajax的get方法发送过来的手机号码
    mobile = request.POST.get('mobile')
    # 通过手机去查找用户是否已经注册
    user = User.objects.filter(uphone=mobile)
    if len(user) != 1:
        return JsonResponse({'msg': "该手机未注册"})
    # 定义一个字符串,存储生成的6位数验证码
    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    # 拼接成发出的短信
    text = "您的验证码是：" + message_code + "。请不要把验证码泄露给其他人。"
    # 把请求参数编码
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    # 请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 通过全局的host去连接服务器
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 得到服务器的响应
    response = conn.getresponse()
    # 获取响应的数据
    response_str = response.read()
    # 关闭连接
    conn.close()
    # 把验证码放进session中
    request.session['message_code'] = message_code
    print(eval(response_str.decode()))
    # 使用eval把字符串转为json数据返回
    return JsonResponse(eval(response_str.decode()))


class LoginView(View):
    def get(self, request):
        """进入登录界面"""
        return render(request, 'demo.html')

    def post(self, request):
        """处理登录操作"""
        # 获取post请求参数
        # 获取手机号/短信验证码
        uphone = request.POST.get('mobile')
        code = request.POST.get('code')
        # 检验合法性
        if not all([uphone, code]):
            return render(request, 'demo.html', {'errmsg': "手机号和短信验证码不能为空"})
        # 业务处理：短信验证码是否正确
        if request.session.get("message_code") != code:
            return render(request, 'demo.html', {'errmsg': "短信验证码错误"})

        # try:
        #     user = User.objects.create_user(uphone, "qq123@qq.com", code, uphone=uphone)  # type: User
        #     user.save()
        # except IntegrityError:
        #     # 判断用户是否存在
        #     return render(request, 'demo.html', {'errmsg': "用户名已存在"})

        # 这是校验用户名和密码的方法，不适用手机校验
        # user = authenticate(uphone=uphone)

        # 根据手机号查找用户
        user = User.objects.filter(uphone=uphone)

        # 判断是否未查找到
        if user[0] is None:
            # 判断用户名和密码是否正确
            return render(request, 'demo.html', {'errmsg': "尚未注册"})

        # 登录成功后,要跳转到next指向的页面
        return render(request, 'index.html')


def pcgetcaptcha(request):
    """极验验证函数"""
    # 校验参数
    user_id = 'test'
    # 创建GeetestLib对象，极验验证码id/key
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    # 验证初始化预处理.换取status,值为0或1
    status = gt.pre_process(user_id)
    # status  user_id存进session中，用于校验
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    # 验证初始化预处理的时候返回的响应的字典转换成的json字符串
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


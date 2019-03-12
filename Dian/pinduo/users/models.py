from django.db import models
#引入django系统用户表
from django.contrib.auth.models import User


#用户信息表
class UserInfo(models.Model):
    #id
    id = models.AutoField(primary_key=True)
    #用户昵称
    nickname = models.CharField(max_length=50, verbose_name="用户名称")
    #用户年龄
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    #用户性别
    gender = models.IntegerField(default=int(float(1)),verbose_name="用户性别")
    #用户头像
    header = models.ImageField(upload_to='static/images/headers/', default="static/images/headers/default.jpg", verbose_name="用户头像")
    #用户电话
    phone = models.CharField(max_length=100,default=1000000000,verbose_name='用户电话'),
    #用户邮箱
    email = models.CharField(max_length=100,default="123456@qq.com",verbose_name="用户邮箱")

    #和系统内置用户管理一对一的关系
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


#用户地址表
class Address(models.Model):
    #用户id
    id = models.AutoField(primary_key=True)
    #收货人
    recv_name = models.CharField(max_length=100, verbose_name="收货人")
    #收货人电话号码
    recv_tel = models.CharField(max_length=20, verbose_name="收货人电话号码")
    #收货人的省份
    province = models.CharField(max_length=100, verbose_name="收货人的省份")
    #收货人的城市
    city = models.CharField(max_length=100, verbose_name="收货人的城市")
    #收货人的县区
    area = models.CharField(max_length=100, verbose_name="收货人的县区")
    #详细地址
    desc = models.CharField(max_length=255, verbose_name="详细地址")
    #是否是默认地址
    is_default = models.BooleanField(default=False, verbose_name="是否是默认地址")
    #地址的所属用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="地址的所属用户")

    def __str__(self):
        return self.recv_name




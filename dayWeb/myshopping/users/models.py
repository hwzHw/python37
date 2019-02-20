from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    #用户呢称
    pickname = models.CharField(max_length=255, unique=True, verbose_name='用户昵称')
    #用户年龄
    age = models.IntegerField(default=18, verbose_name='用户年龄')
    #用户性别
    gender = models.CharField(max_length=10, default='男', verbose_name='用户性别')
    #用户头像
    header = models.ImageField(upload_to='static/imgs/headers', default='static/imgs/headers/xxx.jpg', verbose_name='用户头像')
    #电话
    phone = models.CharField(max_length=50,default='110', verbose_name='电话')
    #身份证
    cusID = models.CharField(max_length=20, verbose_name='身份证')
    #和系统内置的用户管理一对一的关系
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    recv_name = models.CharField(max_length=100, verbose_name='收货人')
    recv_tel = models.CharField(max_length=20, verbose_name='收获人电话')
    province = models.CharField(max_length=100, verbose_name='收获人省份')
    city = models.CharField(max_length=100, verbose_name='收获人城市')
    area = models.CharField(max_length=100, verbose_name='收获人县区')
    street = models.CharField(max_length=255, verbose_name='收获人街道')
    desc = models.CharField(max_length=255, verbose_name='详细地址')
    is_default = models.BooleanField(default=False, verbose_name='是否为默认地址')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='地址所属用户')




















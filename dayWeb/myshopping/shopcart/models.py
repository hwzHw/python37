from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from goods.models import Goods


class ShopCart(models.Model):
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='购物车商品')
    count = models.IntegerField(verbose_name='商品数量')
    addTime = models.DateTimeField(auto_now_add=True, verbose_name='商品添加时间')
    allTotal = models.FloatField(verbose_name='小计金额')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属用户')
from django.db import models

# Create your models here.
from store.models import Store


class GoodsType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name='商品类型名称')
    cover = models.ImageField(upload_to='static/imgs/goods', default='static/imgs/goods/aaa.png', verbose_name='商品类型插图')
    intro = models.TextField(verbose_name='商品类型描述')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父级类型')


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='商品名称')
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.FloatField(verbose_name='商品单价')
    stock = models.IntegerField(verbose_name='库存')
    count = models.IntegerField(default=0, verbose_name='销量')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    intro = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='商品所属商店')
    goodstype = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')


class GoodsImage(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.ImageField(upload_to='static/imgs/goods', default='static/imgs/goods/aaa.png', verbose_name='商品图片')
    status = models.BooleanField(default=False, verbose_name='是否默认显示该图片')
    intro = models.TextField(null=True, blank=True, verbose_name='商品描述')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='所属商品')
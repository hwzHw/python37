from django.db import models
# 导入店铺
# import store
from store.models import Store


#商品类型表
class GoodsType(models.Model):
    #商品id
    id = models.AutoField(primary_key=True)
    #商品类型名称
    name = models.CharField(max_length=255,unique=True,verbose_name="商品类型名称")
    #商品图片
    cover = models.ImageField(upload_to="static/images/goods",default="static/images/goods/default.jpg",verbose_name="商品图片")
    #商品类别描述
    intro = models.TextField(verbose_name="商品类别描述")
    #父级类型(自关联)
    parent = models.ForeignKey('self',null=True,blank=True,verbose_name="父级类型",on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#商品列表
class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    #商品名称
    name = models.CharField(max_length=255,verbose_name="商品名称")
    #商品单价(更准确的表示浮点数的数据Decimal  max_digits有效位数)
    # price = models.DecimalField(max_digits=8,decimal_places=2)
    price = models.FloatField(verbose_name="商品单价")
    #库存
    stock = models.IntegerField()
    #销量
    count = models.IntegerField(default=0)
    #上架时间
    creatTime = models.DateTimeField(auto_now_add=True)
    # 商品介绍
    intro = models.TextField()
    # 构造内键
    store = models.ForeignKey(Store, on_delete=models.CASCADE,verbose_name="商品所属商店")
    #构造外键
    goodstype = models.ForeignKey(GoodsType,on_delete=models.CASCADE,verbose_name="商品类型")

    def __str__(self):
        return self.name


#图片类
class GoodsImages(models.Model):
    id = models.AutoField(primary_key=True)
    #商品图片
    path = models.ImageField(upload_to="static/images/goods",default="static/images/goods/default.jpg",verbose_name="商品图片")
    #商品状态
    status = models.BooleanField(default=False,verbose_name="是否显示该图片")
    #商品图片描述
    intro = models.TextField(verbose_name="商品图片描述",null=True,blank=True)
    #所属商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="所属商品")




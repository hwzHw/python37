from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#一个订单表
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    # 订单所属用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="订单所属用户")
    # 订单生成时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="订单生成时间")
    # 收件人
    recv_name = models.CharField(max_length=100, verbose_name="收件人")
    # 收件人电话
    recv_tel = models.CharField(max_length=50, verbose_name="收件人电话")
    # 收件地址
    recv_address = models.CharField(max_length=255, verbose_name="收件地址")
    # 订单总金额
    all_price = models.FloatField(verbose_name="订单总金额")
    # 订单备注
    remark = models.CharField(max_length=255, verbose_name="订单备注")


#这是一个订单商品表
class orders_item(models.Model):
    id = models.AutoField(primary_key=True)
    # 商品的编号
    goods_id = models.IntegerField(verbose_name="商品编号")
    # 商品图片
    goods_img = models.CharField(max_length=255, verbose_name="商品图片")
    # 商品名称
    goods_name = models.CharField(max_length=100, verbose_name="商品名称")
    # 商品价格
    goods_price = models.FloatField(verbose_name="商品价格")
    # 商品数量
    goods_count = models.IntegerField(verbose_name="商品数量")
    # 商品总价
    goods_price_all = models.FloatField(verbose_name="商品总价")
    # 所属的订单
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="订单")
    def __str__(self):
        return self.goods_name


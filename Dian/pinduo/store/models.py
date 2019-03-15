from django.db import models
from django.contrib.auth.models import User


# 店铺
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    # 店铺名称
    name = models.CharField(max_length=255, unique=True, verbose_name="店铺名称")
    # 店铺图片
    cover = models.ImageField(upload_to="static/images/store", default="static/images/store/default.jpg", verbose_name="店铺图片")
    # 店铺描述
    intro = models.TextField(verbose_name="店铺描述")
    # 开店时间
    opener_time = models.DateTimeField(auto_now_add=True, verbose_name="开店时间")
    # 店铺状态
    status = models.IntegerField(default=0, verbose_name="店铺状态") #0正常营业，1，暂停营业 2永久删除
    # 店铺所属用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所属用户")

    def __str__(self):
        return self.name
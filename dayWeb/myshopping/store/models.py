from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name='店铺名称')
    cover = models.ImageField(upload_to='static/imgs/store', default='static/imgs/store/xxx.jpg',verbose_name='店铺封面')
    intro = models.TextField(verbose_name='店铺描述')
    openTime = models.DateTimeField(auto_now_add=True, verbose_name='开店时间')
    status = models.IntegerField(default=0, verbose_name='店铺状态') #0正常营业  1暂停营业 2永久删除
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='店铺所属')

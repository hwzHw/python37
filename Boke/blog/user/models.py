from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
# Create your models here.



#继承Model父类，来给数据库映射起来
class Users(models.Model):
    #主键 类型写法
    id = models.AutoField(primary_key=True)
    #给到长度限制
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    pwd = models.CharField(max_length=255)
    data = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=20)
    cusID = models.CharField(max_length=20)
    header = models.ImageField(upload_to= 'static/headers/', null=True, blank=True,
                                  default = 'static/headers/xxx.jpg')

    #第三种插入方法  这个语句获得联系
    # userManager = UsersManager()

    #第一种插入方法  类方法
    '''
    @classmethod
    def create_user(cls,name,age):
        user = cls(name=name, age=age)
        return user
    '''
    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='标题')
    # content = models.TextField()
    content = HTMLField(verbose_name='文章内容')
    #1对多的时候，要放在多方
    author=models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='作者', related_name='arts')
    # artmanage = UsersManager()

    def __str__(self):
        return self.title

    #自定义返回文章PK的值
    def get_art_url(self):
        return reverse('user:artshow', kwargs={'pk': self.pk})









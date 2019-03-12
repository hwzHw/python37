from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, verbose_name='用户名称', db_column='uname')
    age = models.IntegerField(default=18)
    genger = models.CharField(max_length=10, default='男')
    address = models.CharField(max_length=255)
    avater = models.CharField(max_length=255, default='static/imgs/123.jpg')

    # model类内置得
    class Meta:
        db_table = 't_user'

    # 1.类方法  通过类名直接调
    # @classmethod
    # def create_user(cls, username, age, genger):
    #     user = cls(username=username, age=age, genger=genger)
    #     return user


class Article(models.Model):
    print(...)
    author = models.ForeignKey(User)
    content = models.TextField()
    title = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)


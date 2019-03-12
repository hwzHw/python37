from django.db import models

# Create your models here.


# 通过属性指向类的管理器
# class AuthorManager(models.Manager):
#     def create_author(self, name, age):
#         author = self.create(name=name, age=age)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    # 类的管理器
    # user = AuthorManager()


    #用来操作数据库在控制台的操作
    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, age):
        author = cls(name=name, age=age)
        return author


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField(verbose_name='文章内容')
    author = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='作者', related_name='arts')
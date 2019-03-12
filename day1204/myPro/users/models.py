from django.db import models


# 2.类的管理器
class UsersManager(models.Manager):
    def create_user(self, name, age):
        user = self.create(name=name, age=age)
        return user


# Create your models here.
# 注意继承model父类   来给数据库映射起来
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)

    usermanager = UsersManager()
# 1.类方法
#     @classmethod
#     def create_user(cls, name, age):
#         users = cls(name=name, age=age)
#         return users
    def __str__(self):
        return self.name
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

    # 一对多时要放在多方
    user = models.ForeignKey(Users, on_delete=models.CASCADE)



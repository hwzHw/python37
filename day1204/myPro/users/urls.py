from django.conf.urls import url
from . import views
urlpatterns = [
    url("^index/$", views.index),
    # 1.方法
    # url("^create/$", views.create),

    # 3.方法
    url("^create/$", views.create, name="create"),

    # 继承时所用到的update
    url("^update/$", views.update, name="update"),


    url("^delete/$", views.delete),

    # 数据库的更改所用到的
    url("^update1/$", views.update1),
    # 位置参数方法1
    url("^(\d+)/param1/$", views.param1),

    # 关键字参数方法2
    url("^(?P<username>\d+)/param2/$", views.param2),

    url("^index1/$", views.index1),

    url("^index2/$", views.index2),

    url("^index3/$", views.index3),

    url("^list/$", views.list, name="list"),

]

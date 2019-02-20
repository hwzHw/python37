from django.conf.urls import url
from . import views



urlpatterns = [
    #确认订单
    url(r'^confirm/$', views.confirm, name='confirm'),
    #支付订单
    url(r'^pay/$', views.pay, name='pay'),
    #生成订单
    url(r'^done/$', views.done, name='done'),
    #查看订单
    url(r'^list/$', views.list, name='list'),
    #订单详情
    url(r'^(\d+)/detail/$', views.detail, name='detail'),
    #删除订单
    url(r'^(\d+)/delete/$', views.delete, name='delete'),

]

















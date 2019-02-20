from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^(?P<count>\d+)/(?P<goods_id>\d+)/add/$', views.add, name='add'),#第一个数字为数量，第二个数字为商品id
    url(r'^list/$', views.list, name='list'),
    #删除购物车商品
    url(r'^(\d+)/delete/$', views.delete, name='delete'),

]
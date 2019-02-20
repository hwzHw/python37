from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(\d+)/add/$', views.add, name='add'),
    url(r'^index/$', views.index, name='index'),
    url(r'^findTypePid/$', views.findTypePid, name='findTypePid'),
    #显示所有商品
    url(r'^(\d+)/list/$', views.list, name='list'),
    #删除商品
    url(r'^(\d+)/(\d+)/delete/$', views.delete, name='delete'),
    #修改商品
    url(r'^(\d+)/update/$', views.update, name='update'),
    #购买时候商品详情
    url(r'^(\d+)/detail/$', views.detail, name='detail'),

]
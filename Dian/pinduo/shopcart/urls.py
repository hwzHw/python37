from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^listt/$", views.listt, name="listt"),         #购物车
    url(r"^add/$", views.add, name="add"),            #添加商品
    # url(r"^shopcar/$", views.shopcar, name="shopcar"),
    url(r"^zj/$", views.zj, name="zj"),       #购物车商品变更
]
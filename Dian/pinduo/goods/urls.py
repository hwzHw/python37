from django.conf.urls import url

from . import views


urlpatterns = [
    # 测试添加商品
    url(r"^add/$", views.add, name="add"),
    # 对应商品ID传到页面的功能
    url(r"^(?P<g_id>\d+)/detail/$", views.detail, name="detail"),
    # 获取商品
    url(r"^findTypeBuId/$", views.findTypeBuId, name="findTypeBuId"),
    url(r"^(?P<s_id>\d+)/(?P<g_id>\d+)/delete_goods/$", views.delete_goods, name="delete_goods"),

]
#
# @Time    : 2019/3/15 14:35
# @Author  : Mat
# @壮      ：Very Cool
# @File    : urls.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................
from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
# 支付宝
    url('admin/', admin.site.urls),
    url('index1/',views.index1),
    url('buy/(?P<ids>\d+)',views.buy),
    url('check_order',views.check_order),
    url('show/',views.show),
    url('order_list',views.order_list),
]
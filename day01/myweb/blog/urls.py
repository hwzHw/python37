#
# @Time    : 2019/2/27 20:21
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
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create_code/$', views.create_code,name='create_code'),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^list/$', views.list),
    url(r'^regist/$', views.regist,name='regist'),
]

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
    url(r'^list/$', views.list),
    # url(r'^register/$', views.register,name='register'),
    url('^login_success/$', views.login_success, name='login_success'),
    url('^register/$', views.register, name='register'),



    url(r'^login', views.LoginView.as_view(), name='login'),
    # 发送短信验证
    url(r'^send_message$', views.send_message, name='send_message'),
    # 极验验证
    url(r'^pc-geetest/register', views.pcgetcaptcha, name='pcgetcaptcha'),

]

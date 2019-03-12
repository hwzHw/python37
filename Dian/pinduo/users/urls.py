from django.conf.urls import url

from . import views

urlpatterns = [
    # 用户登录
    url(r'^user_login/$', views.user_login, name='user_login'),
    # 退出用户登录状态
    url(r'del_login/$', views.del_login, name='del_login'),
    # 注册用户
    url(r'^user_register/$', views.user_register, name='user_register'),
    # 未了解
    url(r'^code/$', views.code, name='code'),
    # 用户首页
    url(r'^index/$', views.index, name='index'),
    # 修改用户
    url(r'^update/$', views.update, name='update'),
    # 传入用户名参数，检查用户名是否存在
    url(r'^(?P<username>\w+)/check_username/$',views.check_username, name='check_username'),
    # 修改用户头像
    url(r'^update_head/$', views.update_head, name='update_head'),
    # 修改用户密码
    url(r'^(?P<u_id>\d+)/update_password/$', views.update_password, name='update_password'),
    # 用户地址列表
    url(r'address_list/$', views.address_list, name='address_list'),
    # 删除用户地址
    url(r'(?P<id>\d+)/delete_address/$', views.delete_address, name='delete_address'),
    # 添加用户地址
    url(r'aaa/$', views.aaa,name='aaa'),
    # 邮箱注册
    url(r'login1/$', views.login1, name='login1'),
    url(r'active/$', views.active, name='active'),
]

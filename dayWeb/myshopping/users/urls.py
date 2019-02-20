from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_register/$', views.user_register, name='user_register'),
    url(r'^index/', views.index, name='index'),

    url(r'^login_success/$', views.login_success, name='login_success'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    #登录成功的主页
    url(r'^user_index/$', views.user_index, name='user_index'),
    #个人资料
    url(r'^user_info/$', views.user_info, name='user_info'),
    #个人资料修改
    url(r'^user_update/$', views.user_update, name='user_update'),
    #退出
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    # 添加收获地址
    url(r'^add_address/$', views.add_address, name='add_address'),
    #查看所有收获地址
    url(r'^list_address/$', views.list_address, name='list_address'),
    #删除收获地址
    url(r'^(\d+)/delete_address/$', views.delete_address, name='delete_address'),
    #修改收获地址
    url(r'^(\d+)/update_address/$', views.update_address, name='update_address'),
]


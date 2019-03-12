from django.conf.urls import url

from . import views
urlpatterns = [
    # 小游戏
    url('^game/$',views.game, name='game'),
    # 捕鱼达人小游戏
    url('^welcome/$',views.welcome, name='welcome'),
    url('^index/$',views.index, name='index'),
    #退出登录
    url('^quit/$',views.quit, name='quit'),

    url('^register/$',views.register, name='register'),
    url('^login_success/$',views.login_success,name='login_success'),
    url('^regist_success/$',views.regist_success,name='regist_success'),

    #个人资料及修改
    url(r'user_detail/$', views.user_detail, name='user_detail'),
    #作者资料
    url(r'^(\d+)/user_otherDetail/$', views.user_otherDetail, name='user_otherDetail'),

    #添加文章
    url('^addArticle/$', views.addArticle,name='addArticle'),
    #修改文章
    url('^updateArticle/$', views.updateArticle,name='updateArticle'),
    #删除文章
    url('^(\d+)/delArticle/$', views.delArticle,name='delArticle'),
    #判断添加文章
    url('addArticle_success/$', views.addArticle_success,name='addArticle_success'),

    #产生验证码
    # url(r'^createCode/$', views.createCode, name='createCode'),
    url(r'^create_code/$', views.create_code, name='create_code'),




    #所有文章
    url('^user_index/$', views.user_index, name='user_index'),
    # 个人文章
    url('^user_articles/$', views.user_articles, name='user_articles'),


]


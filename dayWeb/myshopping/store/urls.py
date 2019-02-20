from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^list/$', views.list, name='list'),
    url(r'^(\d+)/update/$', views.update, name='update'),
    url(r'^(\d+)/detail/$', views.detail, name='detail'),
    url(r'^(\d+)/(\d+)/change/$', views.change, name='change'),

]
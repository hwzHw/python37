from django.conf.urls import url

from . import views

app_name = "store"

urlpatterns = [
    # �������
    url(r"^add/$", views.add, name="add"),
    # չʾȫ��������Ϣ
    url(r"^list/$", views.list, name="list"),
    # ����������ҳ
    url(r"^zhao_shang/$", views.zhao_shang, name="zhao_shang"),
    url(r"^shang_jia/$", views.shang_jia, name="shang_jia"),
    # url(r"^update_store/$",views.update_store,name="update_store"),
    # �޸ĵ���
    url(r"^(?P<s_id>\d+)/update/$", views.update, name="update"),
    # �����Ʒ
    url(r"^(?P<s_id>\d+)/detail/$", views.detail, name="detail"),
    # # ��ͣӪҵ
    # url(r"^(?P<s_id>\d+)/close/$", views.close, name="close"),
    # # ɾ������
    # url(r"^(?P<s_id>\d+)/delete/$", views.delete, name="delete"),
    # ��ʼӪҵ
    url(r"^(?P<s_id>\d+)/(?P<status>\d+)/change/$", views.change, name="change"),
]
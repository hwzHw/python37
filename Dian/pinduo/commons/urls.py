from django.conf.urls import url

from . import views

urlpatterns = [
        # url(r"^wuwu/$", views.wuwu, name="wuwu"),
        url(r"^index/$", views.index, name="index"),
        # url(r"^333$", views.index, name="index"),
]
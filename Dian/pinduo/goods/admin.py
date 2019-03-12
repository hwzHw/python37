from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.GoodsType)
admin.site.register(models.Goods)
admin.site.register(models.GoodsImages)
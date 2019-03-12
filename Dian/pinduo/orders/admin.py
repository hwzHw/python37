from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Orders)
admin.site.register(models.orders_item)

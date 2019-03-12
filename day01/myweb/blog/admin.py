from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_per_page = 2
    fields = ['name', 'username']
admin.site.register(models.Article)

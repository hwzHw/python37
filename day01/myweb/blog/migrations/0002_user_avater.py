# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-05 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avater',
            field=models.CharField(default='/static/imgs/123.jpg', max_length=255),
        ),
    ]

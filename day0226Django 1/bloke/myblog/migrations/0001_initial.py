# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-27 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
    ]
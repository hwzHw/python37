# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-03-11 02:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='订单生成时间')),
                ('recv_name', models.CharField(max_length=100, verbose_name='收件人')),
                ('recv_tel', models.CharField(max_length=50, verbose_name='收件人电话')),
                ('recv_address', models.CharField(max_length=255, verbose_name='收件地址')),
                ('all_price', models.FloatField(verbose_name='订单总金额')),
                ('remark', models.CharField(max_length=255, verbose_name='订单备注')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='订单所属用户')),
            ],
        ),
        migrations.CreateModel(
            name='orders_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_id', models.IntegerField(verbose_name='商品编号')),
                ('goods_img', models.CharField(max_length=255, verbose_name='商品图片')),
                ('goods_name', models.CharField(max_length=100, verbose_name='商品名称')),
                ('goods_price', models.FloatField(verbose_name='商品价格')),
                ('goods_count', models.IntegerField(verbose_name='商品数量')),
                ('goods_price_all', models.FloatField(verbose_name='商品总价')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Orders', verbose_name='订单')),
            ],
        ),
    ]
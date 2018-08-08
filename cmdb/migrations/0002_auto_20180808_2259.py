# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-08 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='buy_user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u8d2d\u4e70\u4eba'),
        ),
        migrations.AlterField(
            model_name='host',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6240\u5c5e\u90e8\u95e8'),
        ),
        migrations.AlterField(
            model_name='host',
            name='keyfile',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='SSH\u79d8\u94a5'),
        ),
        migrations.AlterField(
            model_name='host',
            name='line',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u51fa\u53e3\u7ebf\u8def'),
        ),
        migrations.AlterField(
            model_name='host',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u5236\u9020\u5546'),
        ),
        migrations.AlterField(
            model_name='host',
            name='model',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8d44\u4ea7\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='host',
            name='provider',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u4f9b\u8d27\u5546'),
        ),
        migrations.AlterField(
            model_name='host',
            name='room',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u6240\u5c5e\u673a\u623f'),
        ),
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u72b6\u6001'),
        ),
    ]

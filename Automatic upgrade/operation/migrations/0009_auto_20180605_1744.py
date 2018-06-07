# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-05 17:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0008_auto_20180605_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machine',
            options={'verbose_name': '远程机器', 'verbose_name_plural': '远程机器'},
        ),
        migrations.AddField(
            model_name='machine',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]

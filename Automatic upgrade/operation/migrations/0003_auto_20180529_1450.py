# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_version_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='edition_sn',
            field=models.CharField(default='2.0.1', max_length=20, verbose_name='版本号'),
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.IntegerField(blank=True, default=23, null=True, verbose_name='文件个数'),
        ),
    ]

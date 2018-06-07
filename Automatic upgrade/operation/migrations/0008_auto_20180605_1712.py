# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-05 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_version_is_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_sn', models.CharField(default='1', max_length=20, verbose_name='机器号')),
                ('version_sn', models.CharField(default='2.0.1', max_length=20, verbose_name='版本号')),
            ],
        ),
        migrations.RemoveField(
            model_name='version',
            name='is_update',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-04 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0006_uploadfile_versionfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='is_update',
            field=models.BooleanField(default=False, verbose_name='是否更新'),
        ),
    ]

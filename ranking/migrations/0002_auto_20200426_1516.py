# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-26 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='Mark',
            new_name='mark',
        ),
        migrations.AlterField(
            model_name='mark',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 15, 16, 18, 36003), verbose_name='更新时间'),
        ),
    ]
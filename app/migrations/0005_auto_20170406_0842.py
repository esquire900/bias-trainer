# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170406_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbiasgenerator',
            name='is_higher',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]

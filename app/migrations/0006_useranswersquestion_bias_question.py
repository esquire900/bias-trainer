# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170406_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswersquestion',
            name='bias_question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.QuestionBiasGenerator'),
        ),
    ]

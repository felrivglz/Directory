# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20170317_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='runner',
        ),
        migrations.AddField(
            model_name='runner',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='www.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='runner',
            name='birtday',
            field=models.DateField(),
        ),
    ]

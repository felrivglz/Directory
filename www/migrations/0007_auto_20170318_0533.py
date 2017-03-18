# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20170317_2150'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Distances',
        ),
        migrations.AddField(
            model_name='runner',
            name='metas',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='runner',
            name='image',
            field=models.CharField(max_length=2000),
        ),
    ]
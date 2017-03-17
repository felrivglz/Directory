# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('first_year', models.PositiveSmallIntegerField()),
                ('secon_year', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('birtday', models.DateTimeField()),
                ('category', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]

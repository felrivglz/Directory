# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20170317_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=30)),
                ('weather', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Distances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.CharField(choices=[('100', '100 Metros Planos'), ('200', '200 Metros Planos'), ('400', '400 Metros Planos'), ('800', '800 Metros Planos'), ('1500', '1500 Metros Planos'), ('3000', '3000 Metros Planos'), ('5000', '5000 Metros Planos'), ('10000', '10000 Metros Planos'), ('110v', '110 Metros Con Vallas'), ('400v', '400 Metros Con Vallas')], max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('compentition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Competition')),
            ],
        ),
        migrations.AddField(
            model_name='runner',
            name='distance',
            field=models.CharField(choices=[('100', '100 Metros Planos'), ('200', '200 Metros Planos'), ('400', '400 Metros Planos'), ('800', '800 Metros Planos'), ('1500', '1500 Metros Planos'), ('3000', '3000 Metros Planos'), ('5000', '5000 Metros Planos'), ('10000', '10000 Metros Planos'), ('110v', '110 Metros Con Vallas'), ('400v', '400 Metros Con Vallas')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='time',
            name='runner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Runner'),
        ),
    ]

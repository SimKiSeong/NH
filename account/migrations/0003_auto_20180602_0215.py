# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180602_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0020_auto_20180303_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='cottage',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

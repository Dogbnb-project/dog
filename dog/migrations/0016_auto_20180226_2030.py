# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0015_auto_20180226_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], max_length=100),
        ),
    ]

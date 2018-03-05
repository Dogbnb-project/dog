# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0019_auto_20180303_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], max_length=100),
        ),
    ]
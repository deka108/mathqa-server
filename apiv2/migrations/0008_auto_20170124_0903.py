# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv2', '0007_auto_20170124_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paperset',
            name='title',
        ),
        migrations.AddField(
            model_name='paperset',
            name='name',
            field=models.TextField(null=True),
        ),
    ]

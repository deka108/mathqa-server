# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas_models', '0006_paper_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]

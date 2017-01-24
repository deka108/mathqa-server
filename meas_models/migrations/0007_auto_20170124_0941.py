# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-24 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas_models', '0006_remove_formulaindex_idf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty_level',
            field=models.CharField(choices=[(b'1', b'Very Easy'), (b'2', b'Easy'), (b'3', b'Easy'), (b'4', b'Average'), (b'5', b'Average'), (b'6', b'Average'), (b'7', b'Difficult'), (b'8', b'Difficult'), (b'9', b'Very Difficult'), (b'10', b'Very Difficult')], default='1', max_length=1),
        ),
    ]
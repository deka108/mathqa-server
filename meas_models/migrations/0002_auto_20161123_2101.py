# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 13:01
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meas_models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='number_of_part',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=ckeditor.fields.RichTextField(default='Test'),
        ),
        migrations.DeleteModel(
            name='Part',
        ),
    ]
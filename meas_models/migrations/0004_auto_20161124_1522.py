# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 07:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas_models', '0003_auto_20161124_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answersubpart',
            name='answer_part',
        ),
        migrations.RenameField(
            model_name='answerpart',
            old_name='content',
            new_name='part_content',
        ),
        migrations.RenameField(
            model_name='answerpart',
            old_name='name',
            new_name='part_name',
        ),
        migrations.RenameField(
            model_name='answerpart',
            old_name='respone_type',
            new_name='part_respone_type',
        ),
        migrations.AddField(
            model_name='answerpart',
            name='respone_type_1',
            field=models.CharField(blank=True, choices=[(b'Numberic', b'Exam Numberic'), (b'Sketch', b'Sketch'), (b'EXPRESSION', b'Expression'), (b'Text', b'Text'), (b'Prove', b'Prove')], default=b'Text', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='respone_type_2',
            field=models.CharField(blank=True, choices=[(b'Numberic', b'Exam Numberic'), (b'Sketch', b'Sketch'), (b'EXPRESSION', b'Expression'), (b'Text', b'Text'), (b'Prove', b'Prove')], default=b'Text', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='respone_type_3',
            field=models.CharField(blank=True, choices=[(b'Numberic', b'Exam Numberic'), (b'Sketch', b'Sketch'), (b'EXPRESSION', b'Expression'), (b'Text', b'Text'), (b'Prove', b'Prove')], default=b'Text', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='respone_type_4',
            field=models.CharField(blank=True, choices=[(b'Numberic', b'Exam Numberic'), (b'Sketch', b'Sketch'), (b'EXPRESSION', b'Expression'), (b'Text', b'Text'), (b'Prove', b'Prove')], default=b'Text', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_content_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_content_2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_content_3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_content_4',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_name_1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_name_2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_name_3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='answerpart',
            name='subpart_name_4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='AnswerSubPart',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_seq', models.IntegerField(default=0)),
                ('section_text', models.CharField(max_length=255)),
                ('page_seq', models.IntegerField(default=0)),
                ('page_header', models.TextField(blank=True)),
                ('sub_page_seq', models.IntegerField(default=0)),
                ('sub_page_header', models.TextField(blank=True)),
                ('question_seq', models.IntegerField(default=0)),
                ('question_text', models.TextField(blank=True)),
                ('question_type', models.CharField(choices=[('SingleQuestionTable', 'Single Question Table'), ('SingleQuestionList', 'Single Question List'), ('MultiChoiceQuestion', 'Multi Choice Question'), ('TextQuestion', 'Text Question')], default='SingleQuestionTable', max_length=55)),
                ('sub_question', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=1)),
                ('response_seq', models.IntegerField(default=0)),
                ('response_text', models.CharField(max_length=255)),
                ('response_value', models.IntegerField(default=0)),
                ('response_ops', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], default='N', max_length=1)),
                ('response_columns', models.IntegerField(default=0)),
            ],
        ),
    ]

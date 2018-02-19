# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-12 05:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_lecture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='files',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='date_end',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2018, 2, 12, 5, 46, 36, 113419, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='date_start',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2018, 2, 12, 5, 46, 36, 113419, tzinfo=utc)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-18 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urgencyfr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caau',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='caau',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='inseecitycode',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='inseecitycode',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pdau',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pdau',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]

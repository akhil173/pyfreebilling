# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-17 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0010_auto_20161117_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerratecards',
            name='priority',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], help_text='Priority order, 1 is the\n                                               higher priority and 3 the\n                                               lower one. Correct values\n                                               are : 1 to 7 !.', verbose_name='priority'),
        ),
    ]

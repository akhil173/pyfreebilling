# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-20 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0018_voipswitchprofile_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='voipswitchprofile',
            name='priority',
            field=models.PositiveIntegerField(default=b'0', help_text='Priority.', verbose_name='priority'),
        ),
    ]

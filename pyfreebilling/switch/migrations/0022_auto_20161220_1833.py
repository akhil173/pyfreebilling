# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-20 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0021_voipswitchprofile_outbound_proxy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voipswitchprofile',
            name='outbound_proxy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outboundproxy', to='switch.VoipSwitch', verbose_name='Kamailio server'),
        ),
    ]

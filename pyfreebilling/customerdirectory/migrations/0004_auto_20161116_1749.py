# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-16 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customerdirectory', '0003_auto_20161116_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdirectory',
            name='callee_norm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrules', to='normalizationrule.NormalizationGroup', verbose_name='Destination number normalization rules'),
        ),
        migrations.AlterField(
            model_name='customerdirectory',
            name='callerid_norm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrules', to='normalizationrule.NormalizationGroup', verbose_name='CallerID normalization rules'),
        ),
    ]

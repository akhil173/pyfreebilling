# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-10 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normalizationrule', '0005_auto_20161215_1132'),
        ('customerdirectory', '0009_auto_20161215_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdirectory',
            name='callee_norm_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrulesin', to='normalizationrule.NormalizationGroup', verbose_name='Destination number normalization rules for inbound call'),
        ),
        migrations.AddField(
            model_name='customerdirectory',
            name='callerid_norm_in',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrulesin', to='normalizationrule.NormalizationGroup', verbose_name='CallerID normalization rules for inbound call'),
        ),
        migrations.AlterField(
            model_name='customerdirectory',
            name='callee_norm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrules', to='normalizationrule.NormalizationGroup', verbose_name='Destination number normalization rules for outbound call'),
        ),
        migrations.AlterField(
            model_name='customerdirectory',
            name='callerid_norm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrules', to='normalizationrule.NormalizationGroup', verbose_name='CallerID normalization rules for outbound call'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-15 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0012_auto_20161118_1758'),
        ('switch', '0011_auto_20161215_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoipSwitchProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=b' ', help_text='Description.', max_length=64, verbose_name='Description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('fsswitch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='switch.VoipSwitch', verbose_name='FS server')),
                ('sipprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfreebill.SipProfile', verbose_name='Sip profile')),
            ],
            options={
                'ordering': ('fsswitch', 'sipprofile'),
                'db_table': 'fs_switch_profile',
                'verbose_name': 'FS profile',
                'verbose_name_plural': 'FS profiles',
            },
        ),
    ]

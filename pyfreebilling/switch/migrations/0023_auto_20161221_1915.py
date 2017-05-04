# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-21 18:15
from __future__ import unicode_literals

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0022_auto_20161220_1833'),
    ]

    operations = [
        migrate_sql.operations.ReverseAlterSQL(
            name=b'dispatcher_view',
            sql=b'DROP VIEW IF EXISTS dispatcher CASCADE; ',
            reverse_sql=b"DROP VIEW IF EXISTS dispatcher CASCADE; CREATE OR REPLACE VIEW dispatcher AS  SELECT row_number() OVER () AS id,  fsp.direction,  CONCAT('sip:', fsp.ip, ':', sp.sip_port) AS destination,  0 AS flags,  fsp.priority,  0 AS attrs,  fsp.description FROM fs_switch_profile fsp LEFT JOIN fs_switch f  ON fsp.fsswitch_id = f.id AND fsp.direction = 1 AND f.setid=10 AND f.enabled=TRUE LEFT JOIN sip_profile sp  ON sp.enabled = TRUE AND sp.id = fsp.sipprofile_id; ",
        ),
        migrate_sql.operations.AlterSQL(
            name=b'dispatcher_view',
            sql=b"DROP VIEW IF EXISTS dispatcher CASCADE; CREATE OR REPLACE VIEW dispatcher AS  SELECT row_number() OVER () AS id,  fsp.direction AS setid,  CONCAT('sip:', fsp.ip, ':', sp.sip_port) AS destination,  0 AS flags,  fsp.priority,  0 AS attrs,  fsp.description FROM fs_switch_profile fsp LEFT JOIN fs_switch f  ON fsp.fsswitch_id = f.id AND fsp.direction = 1 AND f.setid=10 AND f.enabled=TRUE LEFT JOIN sip_profile sp  ON sp.enabled = TRUE AND sp.id = fsp.sipprofile_id; ",
            reverse_sql=b'DROP VIEW IF EXISTS dispatcher CASCADE; ',
        ),
    ]

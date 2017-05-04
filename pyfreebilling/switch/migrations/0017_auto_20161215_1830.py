# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-15 17:30
from __future__ import unicode_literals

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0016_auto_20161215_1824'),
    ]

    operations = [
        migrate_sql.operations.CreateSQL(
            name=b'domain_view',
            sql=b'DROP VIEW IF EXISTS domain CASCADE; CREATE OR REPLACE VIEW domain AS  SELECT row_number() OVER () AS id,  domain,  did,  date_modified AS last_modified FROM uid_domain ud;',
            reverse_sql=b'DROP domain',
        ),
    ]

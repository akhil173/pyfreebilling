# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-11 13:22
from __future__ import unicode_literals

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('normalizationrule', '0006_auto_20170111_1402'),
    ]

    operations = [
        migrate_sql.operations.ReverseAlterSQL(
            name=b'dialplan_view',
            sql=b'DROP VIEW IF EXISTS dialplan CASCADE; ',
            reverse_sql=b'DROP VIEW IF EXISTS dialplan CASCADE; CREATE OR REPLACE VIEW dialplan AS SELECT row_number() OVER () AS id, * FROM (  SELECT  n.name,  nrp.dpid_id AS dpid,  nrp.pr,  n.match_op,  n.match_exp,  n.match_len,  n.subst_exp,  n.repl_exp,  n.attrs,  n.description FROM normalization_rule n LEFT JOIN normalization_rule_grp nrp  ON n.id = nrp.rule_id UNION ALL SELECT  name,  dpid,  pr,  match_op,  match_exp,  match_len,  subst_exp,  repl_exp,  attrs,  description FROM call_mapping_rule c) v;',
        ),
        migrate_sql.operations.AlterSQL(
            name=b'dialplan_view',
            sql=b'DROP VIEW IF EXISTS dialplan CASCADE; CREATE OR REPLACE VIEW dialplan AS SELECT row_number() OVER () AS id, * FROM (  SELECT  n.name,  nrp.id AS dpid,  nrp.pr,  n.match_op,  n.match_exp,  n.match_len,  n.subst_exp,  n.repl_exp,  n.attrs,  n.description FROM normalization_rule n LEFT JOIN normalization_rule_grp nrp  ON n.id = nrp.rule_id UNION ALL SELECT  name,  dpid,  pr,  match_op,  match_exp,  match_len,  subst_exp,  repl_exp,  attrs,  description FROM call_mapping_rule c) v;',
            reverse_sql=b'DROP VIEW IF EXISTS dialplan CASCADE; ',
        ),
    ]

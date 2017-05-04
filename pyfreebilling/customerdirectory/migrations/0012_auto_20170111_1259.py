# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-11 11:59
from __future__ import unicode_literals

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('customerdirectory', '0011_auto_20170110_1951'),
    ]

    operations = [
        migrate_sql.operations.ReverseAlterSQL(
            name=b'usrpref_view',
            sql=b'DROP VIEW IF EXISTS usr_preferences CASCADE; ',
            reverse_sql=b"DROP VIEW IF EXISTS usr_preferences CASCADE; CREATE OR REPLACE VIEW usr_preferences AS  SELECT row_number() OVER () AS id,  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallee' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callee_norm_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT row_number() OVER () AS id,  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcaller' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callerid_norm_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT row_number() OVER () AS id,  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcalleein' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callee_norm_in_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT row_number() OVER () AS id,  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallerin' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callerid_norm_in_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True; ",
        ),
        migrate_sql.operations.AlterSQL(
            name=b'usrpref_view',
            sql=b"DROP VIEW IF EXISTS usr_preferences CASCADE; CREATE OR REPLACE VIEW usr_preferences AS SELECT row_number() OVER () AS id, * FROM (  SELECT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallee' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callee_norm_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcaller' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callerid_norm_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcalleein' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callee_norm_in_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True UNION ALL   SELECT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallerin' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nr.id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM customer_directory c INNER JOIN normalization_grp ng   ON ng.id = c.callerid_norm_in_id INNER JOIN normalization_rule_grp nrg  ON nrg.dpid_id = ng.id INNER JOIN normalization_rule nr ON nr.id = nrg.rule_id WHERE c.enabled=True) v; ",
            reverse_sql=b'DROP VIEW IF EXISTS usr_preferences CASCADE; ',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 20:41


from django.db import connection, migrations


def _table_exists(db_cursor, tablename):
    "Returns bool if table exists or not"
    return tablename in connection.introspection.table_names()


class Migration(migrations.Migration):

    dependencies = [("objects", "0008_auto_20170705_1736")]

    db_cursor = connection.cursor()

    if not _table_exists(db_cursor, "objectdb_db_player"):
        # OBS - this is run BEFORE migrations are run!
        operations = []
    else:
        operations = [migrations.RemoveField(model_name="objectdb", name="db_player")]

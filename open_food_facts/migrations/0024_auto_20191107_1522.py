# Generated by Django 2.2 on 2019-11-07 14:22

from django.db import migrations
from django.core.management import call_command


def load_data(apps, schema_editor):
    call_command("loaddata", "data.json")


class Migration(migrations.Migration):

    dependencies = [
        ('open_food_facts', '0023_auto_20191030_1512'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]

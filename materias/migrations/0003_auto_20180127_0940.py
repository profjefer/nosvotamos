# Generated by Django 2.0.1 on 2018-01-27 09:40

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_auto_20161025_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='dados',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
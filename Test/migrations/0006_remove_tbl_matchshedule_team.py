# Generated by Django 5.0.2 on 2024-02-29 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0005_tbl_matchshedule_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_matchshedule',
            name='team',
        ),
    ]

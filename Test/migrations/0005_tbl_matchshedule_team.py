# Generated by Django 5.0.2 on 2024-02-29 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0004_tbl_matchshedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_matchshedule',
            name='team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Test.tbl_team'),
            preserve_default=False,
        ),
    ]

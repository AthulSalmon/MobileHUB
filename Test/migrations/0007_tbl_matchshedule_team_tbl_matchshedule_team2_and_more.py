# Generated by Django 5.0.2 on 2024-02-29 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0006_remove_tbl_matchshedule_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_matchshedule',
            name='team',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='team1_matches', to='Test.tbl_team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_matchshedule',
            name='team2',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='team2_matches', to='Test.tbl_team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tbl_matchshedule',
            name='from_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tbl_matchshedule',
            name='to_Date',
            field=models.DateField(),
        ),
    ]

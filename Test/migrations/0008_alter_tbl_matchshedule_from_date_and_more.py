# Generated by Django 5.0.2 on 2024-02-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0007_tbl_matchshedule_team_tbl_matchshedule_team2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_matchshedule',
            name='from_Date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tbl_matchshedule',
            name='to_Date',
            field=models.CharField(max_length=50),
        ),
    ]

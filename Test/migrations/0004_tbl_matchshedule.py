# Generated by Django 5.0.2 on 2024-02-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0003_tbl_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_matchshedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(max_length=50)),
                ('from_Date', models.CharField(max_length=50)),
                ('to_Date', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
    ]

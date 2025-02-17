# Generated by Django 5.0.2 on 2024-03-05 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guest', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=50)),
                ('complaint_detail', models.CharField(max_length=50)),
                ('complaint_date', models.CharField(max_length=50)),
                ('complaint_reply', models.CharField(max_length=50)),
                ('complaint_replydate', models.CharField(max_length=50)),
                ('complaint_status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.tbl_user')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-19 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0021_tbl_brand_tbl_color'),
        ('guest', '0007_delete_tbl_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='Assets/UserPhoto/')),
                ('user_proof', models.FileField(upload_to='Assets/UserProof/')),
                ('user_status', models.IntegerField(default='0')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.tbl_place')),
            ],
        ),
    ]

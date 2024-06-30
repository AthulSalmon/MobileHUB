# Generated by Django 5.0.2 on 2024-04-24 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCenter', '0001_initial'),
        ('guest', '0011_alter_tbl_shop_shop_address_and_more'),
        ('user', '0014_delete_tbl_servicebooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_servicebooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_detail', models.CharField(max_length=50)),
                ('booking_status', models.IntegerField(default='0')),
                ('booking_fortime', models.CharField(max_length=50)),
                ('booking_fordate', models.DateField(null=True)),
                ('complaint_detail', models.CharField(max_length=50)),
                ('pickup', models.CharField(max_length=10)),
                ('user_number', models.CharField(max_length=50)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceCenter.tbl_service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.tbl_user')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-25 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrator', '0021_tbl_brand_tbl_color'),
        ('guest', '0009_tbl_center_tbl_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_details', models.CharField(max_length=50)),
                ('service_rate', models.CharField(max_length=50)),
                ('service_photo', models.FileField(upload_to='Assets/ServicePhoto/')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.tbl_center')),
                ('servicetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.tbl_servicetype')),
            ],
        ),
    ]

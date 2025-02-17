# Generated by Django 5.0.2 on 2024-04-19 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCenter', '0001_initial'),
        ('Shop', '0006_remove_tbl_product_ram_remove_tbl_product_rom_and_more'),
        ('guest', '0009_tbl_center_tbl_shop'),
        ('user', '0012_delete_tbl_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(max_length=20)),
                ('user_review', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('review_datetime', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ServiceCenter.tbl_service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.tbl_user')),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0018_tbl_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_servicetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stype_name', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-12 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0019_tbl_servicetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_rom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rom_name', models.CharField(max_length=50)),
            ],
        ),
    ]

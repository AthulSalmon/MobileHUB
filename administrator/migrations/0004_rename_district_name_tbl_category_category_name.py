# Generated by Django 5.0.2 on 2024-02-14 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_tbl_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_category',
            old_name='district_name',
            new_name='category_name',
        ),
    ]

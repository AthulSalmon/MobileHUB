# Generated by Django 5.0.2 on 2024-02-20 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_tbl_employee_depatment_tbl_employee_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_employee',
            name='emp_salary',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-20 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_tbl_course_tbl_designation_tbl_employee_tbl_semester_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_name', models.CharField(max_length=50)),
                ('district_id', models.CharField(max_length=50)),
            ],
        ),
    ]

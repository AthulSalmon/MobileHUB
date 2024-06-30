# Generated by Django 5.0.2 on 2024-02-27 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0015_rename_place_name_tbl_place_subcat_name_and_more'),
        ('guest', '0004_delete_tbl_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_admin',
        ),
        migrations.RemoveField(
            model_name='tbl_place',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tbl_course',
            name='department',
        ),
        migrations.RemoveField(
            model_name='tbl_syllabus',
            name='course',
        ),
        migrations.RemoveField(
            model_name='tbl_employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='tbl_employee',
            name='designation',
        ),
        migrations.DeleteModel(
            name='tbl_district',
        ),
        migrations.RemoveField(
            model_name='tbl_syllabus',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='tbl_syllabus',
            name='subject',
        ),
        migrations.DeleteModel(
            name='tbl_category',
        ),
        migrations.DeleteModel(
            name='tbl_place',
        ),
        migrations.DeleteModel(
            name='tbl_course',
        ),
        migrations.DeleteModel(
            name='tbl_department',
        ),
        migrations.DeleteModel(
            name='tbl_designation',
        ),
        migrations.DeleteModel(
            name='tbl_employee',
        ),
        migrations.DeleteModel(
            name='tbl_semester',
        ),
        migrations.DeleteModel(
            name='tbl_subject',
        ),
        migrations.DeleteModel(
            name='tbl_syllabus',
        ),
    ]

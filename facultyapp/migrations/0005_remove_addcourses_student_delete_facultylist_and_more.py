# Generated by Django 5.0.7 on 2024-10-15 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0004_rename_addcourse_addcourses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcourses',
            name='student',
        ),
        migrations.DeleteModel(
            name='FacultyList',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='AddCourses',
        ),
    ]

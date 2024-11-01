# Generated by Django 5.0.7 on 2024-10-16 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_alter_task_created_at'),
        ('facultyapp', '0008_alter_addcourse_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development'), ('OS', 'Operating Systems'), ('SIL', 'Social Immersive Learning')], max_length=50)),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentlist')),
            ],
        ),
    ]

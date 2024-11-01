# Generated by Django 5.0.7 on 2024-10-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development'), ('OS', 'Operating Systems'), ('AIML', 'Artificial Intelligence and Machine Learning'), ('LINUX', 'LINUX Administration')], max_length=50),
        ),
    ]

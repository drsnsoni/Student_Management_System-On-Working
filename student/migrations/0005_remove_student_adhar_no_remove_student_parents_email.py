# Generated by Django 4.1.7 on 2023-05-15 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='adhar_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parents_email',
        ),
    ]

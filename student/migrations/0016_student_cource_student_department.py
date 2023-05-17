# Generated by Django 4.1.7 on 2023-05-17 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_alter_upcoming_event_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cource',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='student.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='student.department'),
        ),
    ]

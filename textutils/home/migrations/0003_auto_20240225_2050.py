# Generated by Django 3.2.24 on 2024-02-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]

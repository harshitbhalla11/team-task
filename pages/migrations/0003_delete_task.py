# Generated by Django 4.2.10 on 2024-03-14 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_task_assigned_to_task_assigned_to'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]

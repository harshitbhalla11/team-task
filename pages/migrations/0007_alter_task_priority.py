# Generated by Django 4.2.10 on 2024-03-15 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, default='low', max_length=10, null=True),
        ),
    ]

# Generated by Django 4.2.10 on 2024-03-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_by_name',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]

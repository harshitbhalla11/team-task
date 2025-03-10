# Generated by Django 4.2.10 on 2024-03-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_brief', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('assigned_to', models.JSONField()),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='low', max_length=10)),
                ('status', models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='not_started', max_length=20)),
                ('labels', models.CharField(blank=True, max_length=100, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='task_attachments/')),
                ('group_id', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
    ]

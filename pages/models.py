from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    admin_user_id = models.CharField(max_length=100)
    admin_user_name = models.CharField(max_length=100, default='NA')
    group_id = models.AutoField(primary_key=True)
    create_date_time = models.DateTimeField(auto_now_add=True)   
    group_members = models.JSONField()
    visibility_type = models.CharField(max_length=20) # public, private
    description = models.CharField(max_length=250,default='NA')
    group_name = models.CharField(max_length=100,default='untitled')

class Task(models.Model):
    PRIORITY = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    STATUS = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    task_id = models.AutoField(primary_key=True)
    task_brief = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.JSONField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY, default='low')
    status = models.CharField(max_length=20, choices=STATUS, default='not_started')
    labels = models.CharField(max_length=100, blank=True, null=True)
    attachments = models.FileField(upload_to='task_attachments/', blank=True, null=True)
    group_id = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)


from django.db import models

class Group(models.Model):
    admin_user_id = models.CharField(max_length=100)
    admin_user_name = models.CharField(max_length=100, default='NA')
    group_id = models.AutoField(primary_key=True)
    create_date_time = models.DateTimeField(auto_now_add=True)   
    group_members = models.JSONField()
    visibility_type = models.CharField(max_length=20) # public, private
    description = models.CharField(max_length=250,default='NA')
    group_name = models.CharField(max_length=100,default='untitled')

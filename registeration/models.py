from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class TeamUser(AbstractUser):
    # Add any custom fields here

    class Meta:
        # You can also define other attributes of your model here
        pass

    # Specify unique related_name values to avoid clash
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        related_name='custom_user_groups',  # Unique related_name
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_permissions',  # Unique related_name
        related_query_name='custom_user_permission',
    )

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_query_name='custom_user',
    )
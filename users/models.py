import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # Указываем уникальные имена для обратных связей
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='группы',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='specific permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions_set",
        related_query_name="user_permission",
    )

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     current_year = models.PositiveIntegerField(default=datetime.datetime.now().year)
#
#     def __str__(self):
#         return self.user.username

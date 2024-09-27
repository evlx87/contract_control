from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('mto', 'MTO User'),
        ('feo', 'FEO User'),
    ]
    role = models.CharField(max_length=3, choices=role_choices)

    # Добавьте здесь другие поля, которые могут быть важны для вашей логики

    def __str__(self):
        return self.user.username


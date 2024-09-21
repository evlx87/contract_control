from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create a superuser and a regular user'

    def handle(self, *args, **options):
        # Создание суперпользователя
        superuser_username = 'admin'
        superuser_password = 'adminpassword'
        superuser = CustomUser.objects.create_superuser(
            username=superuser_username,
            password=superuser_password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()

        self.stdout.write(self.style.SUCCESS(
            f'Superuser {superuser_username} created successfully'))

        # Создание обычного пользователя
        user_username = 'user'
        user_password = 'userpassword'
        user = CustomUser.objects.create_user(
            username=user_username,
            password=user_password)
        user.save()

        self.stdout.write(self.style.SUCCESS(
            f'User {user_username} created successfully'))


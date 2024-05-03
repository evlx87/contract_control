from django.core.management.base import BaseCommand

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        username = 'admin'  # Имя пользователя для создания
        password = 'adminpassword'  # Пароль пользователя

        # Создаем суперпользователя
        user = CustomUser.objects.create_user(
            username=username,
            password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.stdout.write(self.style.SUCCESS(
            f'Superuser {username} created successfully'))

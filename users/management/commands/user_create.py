from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Create a superuser and a regular user'

    def handle(self, *args, **options):
        # Создание суперпользователя
        superuser = CustomUser.objects.create_superuser(
            username='admin',
            password='adminpassword')
        superuser.is_staff = True
        superuser.save()

        self.stdout.write(self.style.SUCCESS(
            'Superuser "admin" created successfully'))

        # Создание обычного пользователя
        user = CustomUser.objects.create_user(
            username='user',
            password='userpassword')

        self.stdout.write(self.style.SUCCESS(
            'User "user" created successfully'))


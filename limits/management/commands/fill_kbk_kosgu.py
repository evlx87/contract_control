from django.core.management.base import BaseCommand

from limits.choice_objects import KBK_TYPE_CHOICES, KOSGU_TYPE_CHOICES
from limits.models import KBK, KOSGU


class Command(BaseCommand):
    help = "Заполняет таблицы KBK и KOSGU данными из переменных KBK_TYPE_CHOICES и KOSGU_TYPE_CHOICES."

    def handle(self, *args, **options):
        self.stdout.write("Создаю записи в таблице KBK...")
        for code, _ in KBK_TYPE_CHOICES:
            KBK.objects.update_or_create(code=code, defaults={'description': f'КБК: {code}'})

        self.stdout.write("Записи в таблице KBK созданы.")

        self.stdout.write("Создаю записи в таблице KOSGU...")
        for code, _ in KOSGU_TYPE_CHOICES:
            KOSGU.objects.update_or_create(code=code, defaults={'description': f'КОСГУ: {code}'})

        self.stdout.write("Записи в таблице KOSGU созданы.")

        self.stdout.write("Все записи успешно созданы.")

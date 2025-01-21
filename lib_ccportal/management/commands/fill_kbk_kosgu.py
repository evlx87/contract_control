from django.core.management.base import BaseCommand

from limits.models import KBK, KOSGU


class Command(BaseCommand):
    help = "Заполняет таблицы KBK и KOSGU данными из переменных KBK_TYPE_CHOICES и KOSGU_TYPE_CHOICES."

    def handle(self, *args, **options):
        self.stdout.write("Создаю записи в таблице KBK...")

        kbk_type_choice = (
            ('417 0702 88 9 00 90059 244', '417 0702 88 9 00 90059 244'),
            ('417 0702 88 9 00 90059 242', '417 0702 88 9 00 90059 242'),
            ('417 0702 88 9 00 90071 244', '417 0702 88 9 00 90071 244'),
            ('417 0702 88 9 00 90071 247', '417 0702 88 9 00 90071 247'),
            ('417 0705 88 9 00 90059 244', '417 0705 88 9 00 90059 244'),
        )

        for code, _ in kbk_type_choice:
            KBK.objects.update_or_create(
                code=code, defaults={
                    'description': f'КБК: {code}'})

        self.stdout.write("Записи в таблице KBK созданы.")

        self.stdout.write("Создаю записи в таблице KOSGU...")

        kosgu_type_choice = (
            ('221', '221'),
            ('222', '222'),
            ('223', '223'),
            ('224', '224'),
            ('225', '225'),
            ('226', '226'),
            ('227', '227'),
            ('310', '310'),
            ('343', '343'),
            ('346', '346'),
            ('349', '349'),
        )

        for code, _ in kosgu_type_choice:
            KOSGU.objects.update_or_create(
                code=code, defaults={
                    'description': f'КОСГУ: {code}'})

        self.stdout.write("Записи в таблице KOSGU созданы.")

        self.stdout.write("Все записи успешно созданы.")

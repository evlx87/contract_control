import json
from datetime import datetime
from decimal import Decimal

from django.core.management.base import BaseCommand

from contracts.models import Contract


class Command(BaseCommand):
    help = 'Loads data from contracts.json into the Contract model'

    def handle(self, *args, **options):
        with open('json/contracts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            contracts_data = data.get('Контракты', [])

            for contract in contracts_data:
                contract_instance = Contract(
                    name=contract.get(
                        'Наименование объекта закупки ',
                        '').strip(),
                    purchase_type=contract.get(
                        'Тип закупки',
                        'ТРУ'),
                    supplier=contract.get(
                        'Поставщик (Исполнитель, подрядчик)',
                        ''),
                    contract_subject=contract.get(
                        'Предмет контракта',
                            ''),
                    contract_number=contract.get(
                        'Номер контракта',
                        ''),
                    contract_date=self.parse_date_str(
                        contract.get('Дата контракта')),
                    contract_duration=self.parse_date_str(
                        contract.get('Срок действия контракта')),
                    service_start_date=self.parse_date_str(
                        contract.get('Дата начала услуг/поставки')),
                    service_end_date=self.parse_date_str(
                        contract.get('Дата окончания услуг/поставки')),
                    contract_amount=Decimal(
                        contract.get(
                            'Сумма контракта',
                            '0.00')))
                contract_instance.save()
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully added contract {contract_instance.contract_number}'))

    def parse_date_str(self, date_str):
        if not date_str:
            return None
        try:
            # Преобразование даты из формата DD.MM.YYYY в объект datetime
            parsed_date = datetime.strptime(date_str, '%d.%m.%Y')
            # Возвращение только даты в формате ISO YYYY-MM-DD (без времени)
            return parsed_date.date().isoformat()
        except ValueError:
            self.stdout.write(self.style.ERROR(
                f"Invalid date format: {date_str}. Date should be in DD.MM.YYYY format"))
            return None

from django.core.management.base import BaseCommand

from contracts.models import PurchaseObject, PurchaseType, ContractType


class Command(BaseCommand):
    help = "Заполняет таблицы объектов закупки, типов закупки и типов контрактов."

    def handle(self, *args, **options):
        # Заполнение PurchaseObject
        purchase_objects = {
            '1-25-001F9125-0001': 'почтовые услуги (в т.ч. франкировальные машины)',
            '1-25-001F9125-0002': 'доставка специальной корреспонденции',
            '1-25-001F9125-0003': 'приобретение активов (марки, конверты с марками и т.д.)',
            '1-25-001F9125-0004': 'услуги привлеченных работников по договорам гражданско-правового характера (с физическими и юридическими лицами)',
            '1-25-001F9125-0005': 'расходы на заключение договоров по перевозке обучающихся на различные мероприятия',
            '1-25-001F9125-0006': 'стирка и химчистка, прочее содержание имущества',
            '1-25-001F9125-0007': 'техническое обслуживание зданий и содержание коммунальных инженерных систем и коммуникаций (по договорам с физическими и юридическими лицами)',
            '1-25-001F9125-0008': 'мойка, техобслуживание и ремонт транспортных средств',
            '1-25-001F9125-0009': 'техническое обслуживание и ремонт прочей аппаратуры и оборудования',
            '1-25-001F9125-0010': 'дезинфекция, дератизация, дезинсекция',
            '1-25-001F9125-0011': 'уборка помещений, содержание в чистоте дворов и имущества (по договорам с физическими и юридическими лицами)',
            '1-25-001F9125-0012': 'услуги подразделений охраны',
            '1-25-001F9125-0013': 'предрейсовые медосмотры',
            '1-25-001F9125-0014': 'расходы по диспансеризации',
            '1-25-001F9125-0015': 'подписка на печатные издания',
            '1-25-001F9125-0016': 'организация питания кадет',
            '1-25-001F9125-0017': 'прочие расходы (услуги по предоставлению мест для стоянки служебного транспорта, услуги и работы по утилизации, нотариальные услуги)',
            '1-25-001F9125-0018': 'страхование автотранспорта',
            '1-25-001F9125-0019': 'обучение, повышение квалификации',
            '1-25-001F9125-0020': 'приобретение ГСМ',
            '1-25-001F9125-0021': 'канцелярские товары',
            '1-25-001F9125-0022': 'бумага',
            '1-25-001F9125-0023': 'бланочная продукция (за исключением бланков строгой отчетности)',
            '1-25-001F9125-0024': 'хозяйственные товары',
            '1-25-001F9125-0025': 'запасные части и расходные материалы для автотранспорта',
            '1-25-001F9125-0026': 'прочие оборотные запасы (материалы)',
            '1-25-001F9125-0027': 'изготовление бланков строгой отчетности',
            '1-25-001F9125-0028': 'прочие материальные запасы однократного применения',
            '1-25-001F9125-0029': 'обращение с ТКО',
            '1-25-001F9125-0030': 'сотовая связь (включая подключение новых сим-карт)',
            '1-25-001F9125-0031': 'абонентская плата (стационарные телефоны)',
            '1-25-001F9125-0032': 'междугородная и международная связь',
            '1-25-001F9125-0033': 'заправка картриджей',
            '1-25-001F9125-0034': 'техобслуживание и ремонт информационно-коммуникационной техники',
            '1-25-001F9125-0035': 'приобретение прикладного и системного программного обеспечения',
            '1-25-001F9125-0036': 'информационно-консультационные услуги в области  компьютерных технологий',
            '1-25-001F9125-0037': 'закупка картриджей',
            '1-25-001F9125-0038': 'запасные части и расходные материалы для ИКТ устройств',
            '1-25-001F9125-0039': 'электроснабжение',
            '1-25-001F9125-0040': 'теплоснабжение',
            '1-25-001F9125-0041': 'горячее водоснабжение',
            '1-25-001F9125-0042': 'холодное водоснабжение',
            '1-25-001F9125-0043': 'водоотведение',
            '1-25-001F9125-0044': 'плата за негативное воздействие на работу ЦВС',
            '1-25-001F9125-0045': 'оказание услуг по обучению педагогических работников и профессиональной переподготовки сотрудников',
            '1-25-001F9125-0104': 'поставка учебной литературы'}

        for code, description in purchase_objects.items():
            PurchaseObject.objects.update_or_create(
                code=code, defaults={'description': description})

        self.stdout.write("Заполнение таблицы объектов закупки завершено.")

        # Заполнение PurchaseType
        purchase_types = [
            ('ТРУ', 'ТРУ'),
            ('п.4 ч.1 ст.93', 'п.4 ч.1 ст.93'),
            ('п.5 ч.1 ст.93', 'п.5 ч.1 ст.93'),
            ('п.8 ч.1 ст.93', 'п.8 ч.1 ст.93'),
            ('п.14 ч.1 ст.93', 'п.14 ч.1 ст.93'),
            ('п.23 ч.1 ст.93', 'п.23 ч.1 ст.93'),
            ('п.29 ч.1 ст.93', 'п.29 ч.1 ст.93')
        ]

        for code, description in purchase_types:
            PurchaseType.objects.update_or_create(
                code=code, defaults={'description': description})

        self.stdout.write("Заполнение таблицы типов закупки завершено.")

        # Заполнение ContractType
        contract_types = [
            ('ГК', 'Государственный контракт'),
            ('Д', 'Договор'),
            ('ПД', 'Платежный документ'),
            ('А', 'Авансовый отчет')
        ]

        for code, description in contract_types:
            ContractType.objects.update_or_create(
                code=code, defaults={'description': description})

        self.stdout.write("Заполнение таблицы типов контрактов завершено.")

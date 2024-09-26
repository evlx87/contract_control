# Generated by Django 5.0.4 on 2024-09-26 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1-25-001F9125-0001', 'почтовые услуги (в т.ч. франкировальные машины)'), ('1-25-001F9125-0002', 'доставка специальной корреспонденции'), ('1-25-001F9125-0003', 'приобретение активов (марки, конверты с марками и т.д.)'), ('1-25-001F9125-0004', 'услуги привлеченных работников по договорам гражданско-правового характера (с физическими и юридическими лицами)'), ('1-25-001F9125-0005', 'расходы на заключение договоров по перевозке обучающихся на различные мероприятия'), ('1-25-001F9125-0006', 'стирка и химчистка, прочее содержание имущества'), ('1-25-001F9125-0007', 'техническое обслуживание зданий и содержание коммунальных инженерных систем и коммуникаций (по договорам с физическими и юридическими лицами)'), ('1-25-001F9125-0008', 'мойка, техобслуживание и ремонт транспортных средств'), ('1-25-001F9125-0009', 'техническое обслуживание и ремонт прочей аппаратуры и оборудования'), ('1-25-001F9125-0010', 'дезинфекция, дератизация, дезинсекция'), ('1-25-001F9125-0011', 'уборка помещений, содержание в чистоте дворов и имущества (по договорам с физическими и юридическими лицами)'), ('1-25-001F9125-0012', 'услуги подразделений охраны'), ('1-25-001F9125-0013', 'предрейсовые медосмотры'), ('1-25-001F9125-0014', 'расходы по диспансеризации'), ('1-25-001F9125-0015', 'подписка на печатные издания'), ('1-25-001F9125-0016', 'организация питания кадет'), ('1-25-001F9125-0017', 'прочие расходы (услуги по предоставлению мест для стоянки служебного транспорта, услуги и работы по утилизации, нотариальные услуги)'), ('1-25-001F9125-0018', 'страхование автотранспорта'), ('1-25-001F9125-0019', 'обучение, повышение квалификации'), ('1-25-001F9125-0020', 'приобретение ГСМ'), ('1-25-001F9125-0021', 'канцелярские товары'), ('1-25-001F9125-0022', 'бумага'), ('1-25-001F9125-0023', 'бланочная продукция (за исключением бланков строгой отчетности)'), ('1-25-001F9125-0024', 'хозяйственные товары'), ('1-25-001F9125-0025', 'запасные части и расходные материалы для автотранспорта'), ('1-25-001F9125-0026', 'прочие оборотные запасы (материалы)'), ('1-25-001F9125-0027', 'изготовление бланков строгой отчетности'), ('1-25-001F9125-0028', 'прочие материальные запасы однократного применения'), ('1-25-001F9125-0029', 'обращение с ТКО'), ('1-25-001F9125-0030', 'сотовая связь (включая подключение новых сим-карт)'), ('1-25-001F9125-0031', 'абонентская плата (стационарные телефоны)'), ('1-25-001F9125-0032', 'междугородная и международная связь'), ('1-25-001F9125-0033', 'заправка картриджей'), ('1-25-001F9125-0034', 'техобслуживание и ремонт информационно-коммуникационной техники'), ('1-25-001F9125-0035', 'приобретение прикладного и системного программного обеспечения'), ('1-25-001F9125-0036', 'информационно-консультационные услуги в области  компьютерных технологий'), ('1-25-001F9125-0037', 'закупка картриджей'), ('1-25-001F9125-0038', 'запасные части и расходные материалы для ИКТ устройств'), ('1-25-001F9125-0039', 'электроснабжение'), ('1-25-001F9125-0040', 'теплоснабжение'), ('1-25-001F9125-0041', 'горячее водоснабжение'), ('1-25-001F9125-0042', 'холодное водоснабжение'), ('1-25-001F9125-0043', 'водоотведение'), ('1-25-001F9125-0044', 'плата за негативное воздействие на работу ЦВС'), ('1-25-001F9125-0045', 'Оказание услуг по обучению педагогических работников и профессиональной переподготовки сотрудников')], max_length=500, verbose_name='Наименование объекта закупки')),
                ('purchase_type', models.CharField(choices=[('ТРУ', 'ТРУ'), ('п. 4 ч. 1 ст. 93', 'п. 4 ч. 1 ст. 93'), ('п. 5 ч. 1 ст. 93', 'п. 5 ч. 1 ст. 93'), ('п. 23 ч. 1 ст. 93', 'п. 23 ч. 1 ст. 93')], max_length=100, verbose_name='Тип закупки')),
                ('supplier', models.CharField(max_length=255, verbose_name='Поставщик (Исполнитель, подрядчик)')),
                ('contract_subject', models.CharField(max_length=500, verbose_name='Предмет контракта')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Номер контракта')),
                ('contract_date', models.DateField(blank=True, null=True, verbose_name='Дата контракта')),
                ('contract_duration', models.DateField(blank=True, null=True, verbose_name='Срок действия контракта')),
                ('service_start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала услуг/поставки')),
                ('service_end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания услуг/поставки')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма контракта')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма оплаты')),
                ('payment_percent', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Процент оплаты')),
                ('contract_file', models.FileField(blank=True, null=True, upload_to='contracts/', verbose_name='Файл контракта')),
                ('contract_type', models.CharField(choices=[('ГК', 'Государственный контракт'), ('Д', 'Договор'), ('ПД', 'Платежный документ'), ('А', 'Авансовый отчет')], max_length=100, verbose_name='Тип контракта')),
                ('kbk_type', models.CharField(choices=[('417 0702 88 9 00 90059 244', '417 0702 88 9 00 90059 244'), ('417 0702 88 9 00 90059 242', '417 0702 88 9 00 90059 242'), ('417 0702 88 9 00 90071 244', '417 0702 88 9 00 90071 244'), ('417 0702 88 9 00 90071 247', '417 0702 88 9 00 90071 247'), ('417 0705 88 9 00 90059 244', '417 0705 88 9 00 90059 244')], max_length=100, verbose_name='КБК')),
                ('kosgu_type', models.CharField(choices=[('221', '221'), ('222', '222'), ('223', '223'), ('224', '224'), ('225', '225'), ('226', '226'), ('227', '227'), ('310', '310'), ('343', '343'), ('346', '346'), ('349', '349')], max_length=100, verbose_name='КОСГУ')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='Дата платежного документа')),
                ('document_name', models.CharField(max_length=255, verbose_name='Наименование и номер документа')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('payment_file', models.FileField(blank=True, null=True, upload_to='payment_docs/', verbose_name='Файл платежного документа')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='contracts.contract', verbose_name='Контракт')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_date', models.DateField(verbose_name='Дата платежного поручения')),
                ('pp_name', models.TextField(verbose_name='Наименование платежного поручения')),
                ('pp_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оплаченная сумма')),
                ('pp_file', models.FileField(blank=True, null=True, upload_to='payment_orders/', verbose_name='Файл платежного поручения')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_orders', to='contracts.contract', verbose_name='Контракт')),
            ],
        ),
    ]

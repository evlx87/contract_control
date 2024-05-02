# Generated by Django 5.0.4 on 2024-05-02 09:59

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
                ('name', models.CharField(max_length=255, verbose_name='Наименование объекта закупки')),
                ('purchase_type', models.CharField(choices=[('ТРУ', 'ТРУ'), ('п. 4 ч. 1 ст. 93', 'п. 4 ч. 1 ст. 93'), ('п. 5 ч. 1 ст. 93', 'п. 5 ч. 1 ст. 93'), ('п. 23 ч. 1 ст. 93', 'п. 23 ч. 1 ст. 93')], max_length=100, verbose_name='Тип закупки')),
                ('funds_allocated', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Доведено в текущем году')),
                ('supplier', models.CharField(max_length=255, verbose_name='Поставщик (Исполнитель, подрядчик)')),
                ('contract_subject', models.CharField(max_length=255, verbose_name='Предмет контракта')),
                ('contract_number', models.CharField(max_length=50, verbose_name='Номер контракта')),
                ('contract_date', models.DateField(verbose_name='Дата контракта')),
                ('contract_duration', models.DateField(verbose_name='Срок действия контракта')),
                ('service_start_date', models.DateField(verbose_name='Дата начала услуг/поставки')),
                ('service_end_date', models.DateField(verbose_name='Дата окончания услуг/поставки')),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма контракта')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма оплаты')),
                ('payment_percent', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Процент оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(verbose_name='Дата платежного документа')),
                ('document_name', models.CharField(max_length=255, verbose_name='Наименование и номер документа')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('pp_name', models.TextField(blank=True, verbose_name='Наименование и дата платежного поручения')),
                ('pp_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оплаченная сумма')),
                ('pp_date', models.DateField(verbose_name='Дата платежного поручения')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='contracts.contract', verbose_name='Контракт')),
            ],
        ),
    ]

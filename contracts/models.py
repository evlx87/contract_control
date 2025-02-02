import os
from decimal import Decimal

from django.db import models

from lib_ccportal.models import PurchaseObject, PurchaseType, ContractType, KBK, KOSGU


# Модель для объектов закупки
class Contract(models.Model):
    name = models.ForeignKey(
        PurchaseObject,
        on_delete=models.CASCADE,
        verbose_name="Наименование объекта закупки"
    )
    purchase_type = models.ForeignKey(
        PurchaseType,
        on_delete=models.CASCADE,
        verbose_name="Тип закупки",
    )
    supplier = models.CharField(
        max_length=255,
        verbose_name="Поставщик (Исполнитель, подрядчик)")
    contract_subject = models.CharField(
        max_length=500,
        verbose_name="Предмет контракта")
    contract_number = models.CharField(
        max_length=50,
        verbose_name="Номер контракта")
    contract_date = models.DateField(
        verbose_name="Дата контракта",
        null=True,
        blank=True)
    contract_duration = models.DateField(
        verbose_name="Срок действия контракта",
        null=True,
        blank=True)
    service_start_date = models.DateField(
        verbose_name="Дата начала услуг/поставки",
        null=True,
        blank=True)
    service_end_date = models.DateField(
        verbose_name="Дата окончания услуг/поставки",
        null=True,
        blank=True)
    contract_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма контракта")
    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма оплаты",
        default=0)
    payment_percent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Процент оплаты",
        default=0,
        null=True)
    contract_file = models.FileField(
        upload_to='contracts/',
        verbose_name="Файл контракта",
        null=True,
        blank=True
    )
    contract_type = models.ForeignKey(
        ContractType,
        on_delete=models.CASCADE,
        verbose_name="Тип контракта"
    )
    kbk_type = models.ForeignKey(
        KBK,
        on_delete=models.CASCADE,
        verbose_name="КБК")
    kosgu_type = models.ForeignKey(
        KOSGU,
        on_delete=models.CASCADE,
        verbose_name="КОСГУ")
    contract_year = models.PositiveIntegerField(
        verbose_name="Год контрактации",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.contract_file:
            original_filename = os.path.basename(self.contract_file.name)
            contract_number_cleaned = self.contract_number.replace('/', '_')
            new_filename = f"{self.contract_type} {contract_number_cleaned} от {self.contract_date} {self.supplier}.pdf"
            self.contract_file.name = os.path.join(
                os.path.dirname(original_filename), new_filename)

        if self.contract_amount and self.payment_amount:
            total_paid = sum(
                payment.pp_amount for payment in self.payments.all())
            self.payment_amount = total_paid
            self.total_balance = self.contract_amount - total_paid
        else:
            self.payment_amount = 0
            self.total_balance = self.contract_amount

        super().save(*args, **kwargs)

    def __str__(self):
        return self.contract_number

    def total_issued_amount(self):
        """ Возвращает сумму всех платежных документов, связанных с этим контрактом """
        return self.payments.aggregate(total=models.Sum('amount'))[
            'total'] or Decimal('0.00')

    def total_pp_issued_amount(self):
        """ Возвращает сумму всех оплат по платежным поручениям, связанным с этим контрактом """
        return sum(
            payment_order.pp_amount for payment_order in self.payment_orders.all())

    def total_balance(self):
        return self.contract_amount - self.total_pp_issued_amount()

    def calculate_payment_percent(self):
        if self.contract_amount != 0:
            total_issued = self.total_pp_issued_amount()
            percent_paid = (total_issued / self.contract_amount) * 100
            return round(percent_paid, 2)
        return 0

    def kbk_full(self):
        return f'{self.kbk_type} {self.kosgu_type}'


class PaymentDocument(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="payments")
    date_issued = models.DateField(
        verbose_name="Дата платежного документа")
    document_name = models.CharField(
        max_length=255,
        verbose_name="Наименование и номер документа")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма")
    payment_file = models.FileField(
        upload_to='payment_docs/',
        verbose_name="Файл платежного документа",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.payment_file:
            original_filename = os.path.basename(self.payment_file.name)
            document_name_cleaned = self.document_name.replace('/', '_')
            new_filename = f"{document_name_cleaned} от {self.date_issued}.pdf"
            self.payment_file.name = os.path.join(
                os.path.dirname(original_filename), new_filename)
        super().save(*args, **kwargs)

    @property
    def issued_amount(self):
        """ Суммирует все выставленные суммы по контракту """
        return PaymentDocument.objects.filter(
            contract=self.contract).aggregate(
            models.Sum('amount'))['amount__sum'] or 0.00

    @property
    def balance(self):
        """ Рассчитывает остаток по контракту """
        total_payable = self.contract.contract_amount
        issued = self.issued_amount
        return total_payable - issued

    def __str__(self):
        return f"{self.document_name} - {self.amount}"


class PaymentOrder(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="payment_orders")
    pp_date = models.DateField(
        verbose_name="Дата платежного поручения")
    pp_name = models.TextField(
        verbose_name="Наименование платежного поручения")
    pp_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Оплаченная сумма")
    pp_file = models.FileField(
        upload_to='payment_orders/',
        verbose_name="Файл платежного поручения",
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.pp_file:
            original_filename = os.path.basename(self.pp_file.name)
            pp_name_cleaned = self.pp_name.replace('/', '_')
            new_filename = f"{pp_name_cleaned} - {self.pp_date}.pdf"
            self.pp_file.name = os.path.join(
                os.path.dirname(original_filename), new_filename)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pp_name} - {self.pp_amount}"


class AdditionalAgreement(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='additional_agreements'
    )
    date = models.DateField(
        verbose_name="Дата соглашения"
    )
    number = models.CharField(
        max_length=50,
        verbose_name="Номер соглашения"
    )
    agreement_file = models.FileField(
        upload_to='agreements/',
        verbose_name="Файл соглашения",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Доп.соглашение от {self.date.strftime('%d.%m.%Y')} №{self.number}"

    def save(self, *args, **kwargs):
        if self.agreement_file:
            contract_type = str(self.contract.contract_type)
            contract_date_str = self.contract.contract_date.strftime('%d.%m.%Y')
            contract_number = self.contract.contract_number
            date_str = self.date.strftime('%d.%m.%Y')
            new_filename = f"ДС_{self.number}_{date_str}_{contract_type}_{contract_date_str}_{contract_number}.pdf"
            self.agreement_file.name = new_filename
        super().save(*args, **kwargs)

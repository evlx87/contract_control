import os
from decimal import Decimal

from django.db import models


# Create your models here.
class Contract(models.Model):
    PURCHASE_TYPE_CHOICES = (
        ('ТРУ', 'ТРУ'),
        ('п. 4 ч. 1 ст. 93', 'п. 4 ч. 1 ст. 93'),
        ('п. 5 ч. 1 ст. 93', 'п. 5 ч. 1 ст. 93'),
        ('п. 23 ч. 1 ст. 93', 'п. 23 ч. 1 ст. 93')
    )

    CONTRACT_TYPE_CHOICES = (
        ('ГК', 'Государственный контракт'),
        ('Д', 'Договор'),
    )

    KBK_TYPE_CHOICES = (
        ('417 0702 88 9 00 90059 244', '417 0702 88 9 00 90059 244'),
        ('417 0702 88 9 00 90059 242', '417 0702 88 9 00 90059 242'),
        ('417 0702 88 9 00 90071 244', '417 0702 88 9 00 90071 244'),
        ('417 0702 88 9 00 90071 247', '417 0702 88 9 00 90071 247'),
        ('417 0705 88 9 00 90059 244', '417 0705 88 9 00 90059 244'),

    )

    KOSGU_TYPE_CHOICES = (
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

    name = models.CharField(
        max_length=255,
        verbose_name="Наименование объекта закупки")
    purchase_type = models.CharField(
        max_length=100,
        verbose_name="Тип закупки",
        choices=PURCHASE_TYPE_CHOICES)
    funds_allocated = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Доведено в текущем году")
    supplier = models.CharField(
        max_length=255,
        verbose_name="Поставщик (Исполнитель, подрядчик)")
    contract_subject = models.CharField(
        max_length=255,
        verbose_name="Предмет контракта")
    contract_number = models.CharField(
        max_length=50,
        verbose_name="Номер контракта")
    contract_date = models.DateField(
        verbose_name="Дата контракта")
    contract_duration = models.DateField(
        verbose_name="Срок действия контракта")
    service_start_date = models.DateField(
        verbose_name="Дата начала услуг/поставки")
    service_end_date = models.DateField(
        verbose_name="Дата окончания услуг/поставки")
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
    contract_type = models.CharField(
        max_length=100,
        verbose_name="Тип контракта",
        choices=CONTRACT_TYPE_CHOICES)
    kbk_type = models.CharField(
        max_length=100,
        verbose_name="КБК",
        choices=KBK_TYPE_CHOICES)
    kosgu_type = models.CharField(
        max_length=100,
        verbose_name="КОСГУ",
        choices=KOSGU_TYPE_CHOICES)

    def save(self, *args, **kwargs):
        if self.contract_file:
            original_filename = os.path.basename(self.contract_file.name)
            new_filename = f"{self.contract_type} {self.contract_number} от {self.contract_date} - {self.supplier}.pdf"
            self.contract_file.name = os.path.join(
                os.path.dirname(original_filename), new_filename)
        super().save(*args, **kwargs)

        if self.contract_amount and self.payment_amount:
            total_paid = sum(
                payment.pp_amount for payment in self.payments.all())
            self.payment_amount = total_paid
            self.total_balance = self.contract_amount - total_paid
            super().save(*args, **kwargs)
        else:
            self.payment_amount = 0
            self.total_balance = self.contract_amount
            super().save(*args, **kwargs)

    def total_issued_amount(self):
        """ Возвращает сумму всех счетов, связанных с этим контрактом """
        return self.payments.aggregate(total=models.Sum('amount'))[
            'total'] or Decimal('0.00')

    def total_balance(self):
        return self.contract_amount - self.total_issued_amount()


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
            new_filename = f"{self.document_name} от {self.date_issued}.pdf"
            self.payment_file.name = os.path.join(os.path.dirname(original_filename), new_filename)
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
            new_filename = f"{self.pp_name} - {self.pp_date}.pdf"
            self.pp_file.name = os.path.join(
                os.path.dirname(original_filename), new_filename)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pp_name} - {self.pp_amount}"

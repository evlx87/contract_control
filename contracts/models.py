from django.db import models


# Create your models here.
class Purchase(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование объекта закупки")
    purchase_type = models.CharField(max_length=100, verbose_name="Тип закупки")
    year_published = models.IntegerField(verbose_name="Доведено в текущем году")
    supplier = models.CharField(max_length=255, verbose_name="Поставщик (Исполнитель, подрядчик)")
    contract_subject = models.CharField(max_length=255, verbose_name="Предмет контракта")
    contract_number = models.CharField(max_length=50, verbose_name="Номер контракта")
    contract_date = models.DateField(verbose_name="Дата контракта")
    contract_duration = models.IntegerField(verbose_name="Срок действия контракта")
    service_start_date = models.DateField(verbose_name="Дата начала услуг/поставки")
    service_end_date = models.DateField(verbose_name="Дата окончания услуг/поставки")
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма контракта")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    payment_percent = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Процент оплаты")

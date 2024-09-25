from django.db import models

from contracts.models import Contract


# Create your models here.
class Limit(models.Model):

    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        verbose_name="Контракт",
        related_name="limit"
    )
    contract_name = models.CharField(
        max_length=500,
        verbose_name="Наименование объекта закупки"
    )
    contract_date = models.DateField(
        verbose_name="Дата контракта"
    )
    contract_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма контракта"
    )

    def save(self, *args, **kwargs):
        self.contract_name = self.contract.name
        self.contract_date = self.contract.contract_date
        self.contract_amount = self.contract.contract_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.contract_name} - {self.contract_amount}"
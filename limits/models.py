import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from contracts.models import Contract


# Create your models here.
class KBK(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.code


class KOSGU(models.Model):
    code = models.CharField(max_length=6, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.code


class Limit(models.Model):
    name = models.CharField(max_length=300)
    kbk = models.ForeignKey(KBK, on_delete=models.PROTECT, related_name='limits')
    kosgu = models.ForeignKey(KOSGU, on_delete=models.PROTECT, related_name='limits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_limit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    year = models.PositiveIntegerField(default=datetime.datetime.now().year)

    def __str__(self):
        return self.name


# Сигнал для обновления остатка лимита при создании контракта
@receiver(post_save, sender=Contract)
def update_remaining_limit(sender, instance, created, **kwargs):
    if created:
        try:
            limit = Limit.objects.get(
                kbk=instance.kbk_type,
                kosgu=instance.kosgu_type,
                year=instance.contract_date.year
            )
            limit.remaining_limit -= instance.contract_amount
            limit.save(update_fields=['remaining_limit'])
        except Limit.DoesNotExist:
            pass

# Сигнал для проверки превышения лимита при сохранении контракта


@receiver(pre_save, sender=Contract)
def check_limit_exceeded(sender, instance, **kwargs):
    try:
        limit = Limit.objects.get(
            kbk=instance.kbk_type,
            kosgu=instance.kosgu_type,
            year=instance.contract_date.year
        )
        if instance.contract_amount > limit.remaining_limit:
            raise ValidationError("Превышен лимит финансирования.")
    except Limit.DoesNotExist:
        pass

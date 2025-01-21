from django.db import models

# Create your models here.
class PurchaseObject(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.description


# Модель для типа закупки
class PurchaseType(models.Model):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.description


# Модель для типа контракта
class ContractType(models.Model):
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.description

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


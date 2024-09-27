from django.db import models


# Create your models here.
class Limit(models.Model):
    name = models.CharField(max_length=300)
    kbk_type = models.CharField(max_length=26)
    kosgu_type = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_limit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

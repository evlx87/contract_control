from django.contrib import admin
from .models import Contract
from .forms import ContractForm


# Register your models here.
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    form = ContractForm

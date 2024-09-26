from django.shortcuts import render
from .models import Limit
from .choice_objects import PURCHASE_ODJ_CHOICE


def limit_card(request):
    limit_data = Limit.objects.all()  # Получаем все данные из модели Limit
    limit_info = []
    for limit in limit_data:
        purchase_obj = PURCHASE_ODJ_CHOICE.get(limit.contract.contract_number, '')
        limit_info.append(f"{limit.contract.contract_number} {purchase_obj} - КБК {limit.contract.kbk_type} КОСГУ {limit.contract.kosgu_type}")
    return render(request,
                  'limits/limits_card.html',
                  {'limit_data': limit_info})

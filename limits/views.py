from django.shortcuts import render, redirect

from contracts.models import Contract
from .choice_objects import PURCHASE_ODJ_CHOICE
from .forms import LimitForm
from .models import Limit


# def limit_card(request):
#     limit_data = Limit.objects.all()
#     limit_info = []
#     for limit in limit_data:
#         purchase_obj = PURCHASE_ODJ_CHOICE.get(limit.contract.contract_number, '')
#         limit_info.append(f"{purchase_obj} - КБК {limit.contract.kbk_type} КОСГУ {limit.contract.kosgu_type}")
#     return render(request, 'limits/limits_card.html', {'limit_data': limit_info})
def limit_card(request):
    limits = Limit.objects.all()
    return render(request, 'limits/limits_card.html', {'limits': limits})


def add_limit(request):
    if request.method == 'POST':
        form = LimitForm(request.POST)
        if form.is_valid():
            limit = form.save(commit=False)
            # Найдем все контракты с соответствующим КБК и КОСГУ
            contracts = Contract.objects.filter(kbk_type=limit.kbk_type, kosgu_type=limit.kosgu_type)
            # Вычитаем суммы контрактов из доведенных лимитов
            total_contract_amount = sum(contract.amount for contract in contracts)
            remaining_limit = limit.amount - total_contract_amount
            limit.remaining_limit = remaining_limit
            limit.save()
            return redirect('limits:limit_card')
    else:
        form = LimitForm()
    return render(request, 'limits/add_limit.html', {'form': form})

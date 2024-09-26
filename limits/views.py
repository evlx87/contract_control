from django.shortcuts import render, redirect

from .choice_objects import PURCHASE_ODJ_CHOICE
from .forms import LimitForm
from .models import Limit


def limit_card(request):
    limit_data = Limit.objects.all()
    limit_info = []
    for limit in limit_data:
        purchase_obj = PURCHASE_ODJ_CHOICE.get(limit.contract.contract_number, '')
        limit_info.append(f"{purchase_obj} - КБК {limit.contract.kbk_type} КОСГУ {limit.contract.kosgu_type}")
    return render(request, 'limits/limits_card.html', {'limit_data': limit_info})


def add_limit(request):
    if request.method == 'POST':
        form = LimitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('limits:limit_card')
    else:
        form = LimitForm()
    return render(request, 'limits/add_limit.html', {'form': form})
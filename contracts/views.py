from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from contracts.forms import ContractForm
from contracts.models import Contract


# Create your views here.
class IndexView(TemplateView):
    template_name = 'contracts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'
        return context


class AddContractView(View):
    def get(self, request):
        form = ContractForm()
        return render(request, 'contracts/purchase_add.html', {'form': form})

    def post(self, request):
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contracts/')  # Redirect to the main page after adding, modify as needed
        return render(request, 'contracts/purchase_add.html', {'form': form})


class PurchaseListView(ListView):
    model = Contract
    template_name = 'contracts/purchases_list.html'  # Указываем имя шаблона
    context_object_name = 'purchases'  # Как будет называться переменная в шаблоне

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Закупки'
        return context


def contract_detail(request, contract_number):
    contract = Contract.objects.get(contract_number=contract_number)
    return render(request, 'contracts/contract_detail.html', {'contract_detail': contract})

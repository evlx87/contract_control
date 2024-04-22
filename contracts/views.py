from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from contracts.forms import PaymentDocumentForm, ContractForm
from contracts.models import Contract, PaymentDocument


# Create your views here.
class IndexView(TemplateView):
    template_name = 'contracts/index.html'


# def add_contract(request):
#     if request.method == 'POST':
#         form = ContractForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/contracts/')  # Перенаправление на главную страницу после добавления, измените это по надобности
#     else:
#         form = ContractForm()
#     return render(request, 'contracts/purchase_add.html', {'form': form})
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

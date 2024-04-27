from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from contracts.forms import ContractForm, PaymentDocumentForm
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
            return redirect('/contracts/')
        return render(request, 'contracts/purchase_add.html', {'form': form})


class PurchaseListView(ListView):
    model = Contract
    template_name = 'contracts/purchases_list.html'
    context_object_name = 'purchases'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Закупки'
        return context


def contract_detail(request, contract_number):
    contract = get_object_or_404(Contract, contract_number=contract_number)
    return render(request, 'contracts/contract_detail.html', {'contract_detail': contract})


class AddPaymentDocView(View):
    template_name = 'contracts/payment_doc_add.html'

    def get_contract(self, contract_id):
        return get_object_or_404(Contract, id=contract_id)

    def get(self, request, contract_id=None):
        contract = None
        if contract_id:
            contract = self.get_contract(contract_id)
            form = PaymentDocumentForm(initial={'contract': contract})
        else:
            form = PaymentDocumentForm()
        return render(request, self.template_name, {'form': form, 'contract': contract})

    def post(self, request, contract_id):
        contract = self.get_contract(contract_id)
        form = PaymentDocumentForm(request.POST)
        if form.is_valid():
            payment_document = form.save(commit=False)
            payment_document.contract = contract
            payment_document.save()
            return redirect('contracts:contract-detail', contract_number=contract.contract_number)
        return render(request, self.template_name, {'form': form, 'contract': contract})

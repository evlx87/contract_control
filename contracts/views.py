from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, TemplateView

from contracts.forms import ContractForm, PaymentDocumentForm, PaymentOrderForm
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
        form = ContractForm(request.POST, request.FILES)
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


def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request,
                  'contracts/contract_detail.html',
                  {'contract_detail': contract})


def contract_edit(request, contract_id):
    contract = Contract.objects.get(pk=contract_id)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', pk=contract.id)
    else:
        form = ContractForm(instance=contract)

    return render(request, 'contracts/contract_edit.html', {'form': form, 'contract': contract})


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
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

    def post(self, request, contract_id):
        contract = self.get_contract(contract_id)
        form = PaymentDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            payment_document = form.save(commit=False)
            payment_document.contract = contract
            payment_document.save()
            return redirect(
                'contracts:contract-detail',
                contract_number=contract.contract_number)
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})


class AddPaymentOrderView(View):
    template_name = 'contracts/payment_order_add.html'

    def get(self, request, contract_id=None):
        contract = get_object_or_404(Contract, id=contract_id)
        form = PaymentOrderForm(initial={'contract': contract})
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

    def post(self, request, contract_id):
        contract = get_object_or_404(Contract, id=contract_id)
        form = PaymentOrderForm(request.POST, request.FILES)
        if form.is_valid():
            payment_order = form.save(commit=False)
            payment_order.contract = contract
            payment_order.save()
            return redirect(
                'contracts:contract-detail',
                contract_number=contract.contract_number)
        return render(
            request, self.template_name, {
                'form': form, 'contract': contract})

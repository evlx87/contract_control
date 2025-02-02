from django.urls import path

from contracts.views import PurchaseListView, IndexView, AddContractView, AddPaymentDocView, \
    AddPaymentOrderView, contract_edit, contract_delete, JournalListView, export_to_excel, AddAdditionalAgreementView, \
    ContractDetailView

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('contracts/journal', JournalListView.as_view(), name='journal_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contract/<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),
    path('contract/<int:contract_id>/edit/', contract_edit, name='contract-edit'),
    path('contract/<int:pk>/delete/', contract_delete, name='contract-delete'),
    path('contract/<int:contract_id>/add_doc', AddPaymentDocView.as_view(), name='add_payment_doc'),
    path('contract/<int:contract_id>/add_order', AddPaymentOrderView.as_view(), name='add_payment_order'),
    path('export-excel/', export_to_excel, name='export_excel'),
    path('contract/<int:contract_id>/add_agreement/', AddAdditionalAgreementView.as_view(), name='add_additional_agreement'),
]

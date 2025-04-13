from django.urls import path

from contracts.views import PurchaseListView, IndexView, AddContractView, AddPaymentDocView, AddPaymentOrderView, \
    JournalListView, AddAdditionalAgreementView, ContractDetailView, ExportToExcelView, ContractEditView, \
    ContractDeleteView, AdditionalAgreementDetailView

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('contracts/journal', JournalListView.as_view(), name='journal_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contract/<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),
    path('contract/<int:contract_id>/edit/', ContractEditView.as_view(), name='contract-edit'),
    path('contract/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract-delete'),
    path('contract/<int:contract_id>/add_doc', AddPaymentDocView.as_view(), name='add_payment_doc'),
    path('contract/<int:contract_id>/add_order', AddPaymentOrderView.as_view(), name='add_payment_order'),
    path('export-excel/', ExportToExcelView.as_view(), name='export_excel'),
    path('contract/<int:contract_id>/add_agreement/', AddAdditionalAgreementView.as_view(), name='add_additional_agreement'),
    path('contract/<int:contract_id>/additional_agreement/<int:pk>/', AdditionalAgreementDetailView.as_view(), name='additional-agreement-detail'),
]

from django.urls import path

from contracts.views import PurchaseListView, IndexView, AddContractView, contract_detail, AddPaymentDocView, \
    AddPaymentOrderView, contract_edit

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contract/<int:pk>/', contract_detail, name='contract-detail'),
    path('contract/<int:contract_id>/edit/', contract_edit, name='contract-edit'),
    path('contract/<int:contract_id>/add_doc', AddPaymentDocView.as_view(), name='add_payment_doc'),
    path('contract/<int:contract_id>/add_order', AddPaymentOrderView.as_view(), name='add_payment_order')
]

from django.urls import path

from contracts.views import PurchaseListView, IndexView, AddContractView, contract_detail

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contracts/', PurchaseListView.as_view(), name='purchase_list'),
    path('add/', AddContractView.as_view(), name='add_contract'),
    path('contracts/<str:contract_number>/', contract_detail, name='contract-detail'),
]

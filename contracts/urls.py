from django.urls import path

from contracts.views import IndexView

app_name = 'contracts'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

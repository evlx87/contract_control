from django.urls import path
from limits.views import limit_card, add_limit

app_name = 'limits'

urlpatterns = [
    path('limit-card/', limit_card, name='limit_card'),
    path('add-limit/', add_limit, name='add_limit'),
]


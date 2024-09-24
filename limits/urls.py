from django.urls import path

from limits.views import limit_card

app_name = 'limits'

urlpatterns = [
    path('limit-card/', limit_card, name='limit_card'),
]

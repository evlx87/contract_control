from django.urls import path
from limits.views import AddLimitView, LimitCardView

app_name = 'limits'

urlpatterns = [
    path('limit-card/', LimitCardView.as_view(), name='limit_card'),
    path('add-limit/', AddLimitView.as_view(), name='add_limit'),
]


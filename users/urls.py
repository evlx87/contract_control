from django.urls import path

from users.views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]


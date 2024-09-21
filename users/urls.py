from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .forms import CustomAuthenticationForm

app_name = 'users'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='users/login.html',
                           authentication_form=CustomAuthenticationForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class CustomLoginView(View):
    def get(self, request):
        # Отобразить страницу входа
        return render(request, 'registration/login.html')

    def post(self, request):
        # Обработка запроса на вход
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})  # Успешный вход
        else:
            return JsonResponse({"error": "Пожалуйста, введите правильные имя пользователя и пароль."}, status=400)
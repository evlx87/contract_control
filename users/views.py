from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})  # Успешный вход
        else:
            return JsonResponse({"error": "Пожалуйста, введите правильные имя пользователя и пароль."}, status=400)

    return render(request, 'registration/login.html')
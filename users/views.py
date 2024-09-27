from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contracts:index')
        else:
            # Обработка ошибки неверных учетных данных
            pass
    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('contracts:index')


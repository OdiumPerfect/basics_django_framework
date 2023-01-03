from django.contrib import auth
from django.shortcuts import render
from authapp.forms import UserLoginForm


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
    else:
        form = UserLoginForm()

    context = {
        'title': 'Geekshop | Авторизация',
        'form' : form
    }
    return render(request, 'authapp/login.html', context)

def register(request):
    context = {
        'title': 'Geekshop | Регистрация'
    }
    return render(request, 'authapp/register.html', context)

def logout(request):
    pass

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm



# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def tasks(request):
    return render(request, 'tasks.html')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def register_login(request):
    register_form = RegisterForm()
    login_form = AuthenticationForm()
    error = None
    if request.method == 'POST':
        if 'register' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                try:
                    user = register_form.save()
                    login(request, user) 
                    return redirect('tasks')  
                except IntegrityError:
                    error = 'El usuario ya existe.'

        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('tasks')
            else:
                error = 'Usuario o contraseña incorrectos.'

    return render(request, 'register_login.html', {
        'register_form': register_form,
        'login_form': login_form,
        'error': error
    })
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import LoginForm, RegisterForm


def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        print('Logged in ...')
    return render(request, 'accounts/login.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        form.save(request)
        return redirect('login')
    else:
        print('in else')
        return render(request,'accounts/register.html', context)
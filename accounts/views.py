from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditUserForm, ProfileForm
from django.contrib import messages, auth
from listings.models import Listing
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


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
        messages.success(request, 'You are now logged in')
        return redirect('profile-account')
    return render(request, 'accounts/login.html', context)


def register(request):
    form = RegisterForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        print(form.save())
        return redirect('login')
    else:
        return render(request, 'accounts/register.html', context)


def profile_account(request):
    photo_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    form = EditUserForm(instance=request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        form.save(request)
        photo_form.save()
    context = {
        'form': form,
        'photo_form': photo_form,
    }
    return render(request, 'accounts/profile-account.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # In order to keep the user logged in
            update_session_auth_hash(request, form.user)
            return redirect('profile-account')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'accounts/change_password.html', context)





def test(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile-account')
    else:
        form = ProfileForm(instance=request.user.profile)
        context = {
            'form': form
        }
        return render(request, 'accounts/test.html', context)



from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from AuthorLoginApp.forms import SignupForm,Authentication_Form,ChangeEmailForm
from django.contrib.auth.forms import PasswordChangeForm
from AuthorLoginApp.models import User
from django.contrib.auth.decorators import login_required
from AuthorLoginApp import models

# Create your views here.

def signup_view (request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('NewsApp:home'))
    else:
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('AuthorLoginApp:login'))
    return render(request, 'AuthorLoginApp/signup.html', {'form': form, 'title':'Author Signup'})


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('NewsApp:home'))
    else:
        form = Authentication_Form()
        if request.method == 'POST':
            form = Authentication_Form(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse('NewsApp:home'))
        return render(request, 'AuthorLoginApp/login.html', {'form': form, 'title': 'Admin Login'})
    
@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, 'Logged out successfully!')
        return HttpResponseRedirect(reverse('NewsApp:home'))
    

@login_required
def change_password_view(request):
    form = PasswordChangeForm( user=request.user )
    if request.method == 'POST':
        form = PasswordChangeForm( data=request.POST, user=request.user)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return HttpResponseRedirect(reverse('NewsApp:home'))
    return render(request, 'AuthorLoginApp/password_change.html', {'form': form, 'title': 'Change Password'})


@login_required
def change_email(request):
    form = ChangeEmailForm(instance=request.user)
    if request.method == 'POST':
        form = ChangeEmailForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email changed successfully!')
            return HttpResponseRedirect(reverse('NewsApp:home'))
    return render(request, 'AuthorLoginApp/change_email.html', {'form': form, 'title': 'Change Email'})

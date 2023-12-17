from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                messages.success(request, 'Logged in successfully')
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')
    
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')



def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password changed successfully')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user = request.user)
        return render(request, 'change_pass.html', {'form': form})
    else:
        return redirect('profile')
    
def change_password2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password changed successfully without old password')
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'change_pass.html', {'form': form})
    else:
        return redirect('profile')
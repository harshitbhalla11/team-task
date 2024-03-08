from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

@login_required
def home(request):
    return render(request, 'home-page.html', {})

def entry_view(request):
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})    
    else:
        return render(request, 'landing-page.html', {})

def authenticationView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None )
        if form.is_valid():
            form.save()
            return redirect('login/')
    return render(request, 'registration/register.html',{'form' :form})

from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = 'Invalid username or password'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 
 

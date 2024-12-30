from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {'form': UserCreationForm()})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(form.cleaned_data['username'], password=form.cleaned_data['password1'])
                user.save()
                login(request, user)
                messages.success(request, 'Usuario creado correctamente')
                return redirect('tasks')
            except:
                messages.error(request, 'Error al crear el usuario')
        else:
            messages.error(request, form.errors)
            return render(request, 'singup.html', {'form': form})
        
def tasks(request):
    return render(request, 'tasks.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html', {'form': AuthenticationForm()})
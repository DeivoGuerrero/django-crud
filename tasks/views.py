from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from .forms import TaskForm

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
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'tasks.html', {'tasks': tasks})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task(title=form.cleaned_data['title'], description=form.cleaned_data['description'], completed=form.cleaned_data['completed'], user=request.user)
            task.save()
            messages.success(request, 'Tarea creada correctamente')
            return redirect('tasks')
        else:
            messages.error(request, form.errors)
            return render(request, 'tasks.html', {'form': form})

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
        
def edit_task(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'form': form})
    elif request.method == 'POST':
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizada correctamente')
            return redirect('tasks')
        else:
            messages.error(request, form.errors)
            return render(request, 'edit_task.html', {'form': form})
    
    
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request, 'Tarea eliminada correctamente')
    return redirect('tasks')
    

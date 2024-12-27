from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
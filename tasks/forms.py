from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Usuario

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombres', 'apellidos', 'password1', 'password2']
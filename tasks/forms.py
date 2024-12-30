from django import forms
from .models import Task

class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if instance:
            self.fields['title'].initial = instance.title
            self.fields['description'].initial = instance.description
            self.fields['completed'].initial = instance.completed
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['completed'].widget.attrs.update({'class': 'form-check-input'})


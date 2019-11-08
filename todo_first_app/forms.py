from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    path = forms.CharField(required=False)
    class Meta:
        model = Task
        fields="__all__"

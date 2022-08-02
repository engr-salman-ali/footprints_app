from django import forms
from todolist_app.models import TodoList

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task','done']
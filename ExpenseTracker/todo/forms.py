from django import forms
from django.forms import ModelForm
from .models import Todo, STATUS, PRIORITY


class CreateTodo(ModelForm):
    status = forms.ChoiceField(choices=STATUS, widget=forms.RadioSelect())
    priority = forms.ChoiceField(choices=PRIORITY, widget=forms.RadioSelect())
    task = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user']


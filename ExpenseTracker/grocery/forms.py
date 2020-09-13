from django import forms
from .models import List, Item
from django.forms import ModelForm


class CreateList(ModelForm):
    name = forms.CharField(label="Enter name of your list",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = List
        fields = '__all__'
        exclude = ['user']


class CreateItem(ModelForm):
    name = forms.CharField(label="Enter name of your Item",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Item
        fields = '__all__'

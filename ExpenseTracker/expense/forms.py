from django import forms
from django.forms import ModelForm
from .models import ExpenseItem, ExpenseProfile

# priority = forms.ChoiceField(choices=PRIORITY, widget=forms.RadioSelect())


class CreateExpense(ModelForm):
    date_purchased = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = ExpenseItem
        fields = '__all__'
        exclude = ['userProfile']


class AddBudget(ModelForm):
    class Meta:
        model = ExpenseProfile
        fields = "__all__"
        exclude = ['user']

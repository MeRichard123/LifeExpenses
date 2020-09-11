from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
    return redirect('grocery_view')


@login_required(login_url='login')
def delete_list(request, pk):
    userlist = List.objects.get(id=pk)
    if request.method == "POST":
        userlist.delete()
    return redirect('grocery_view')

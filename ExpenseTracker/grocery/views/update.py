from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import CreateItem, CreateList


@login_required(login_url='login')
def update_list(request, pk):
    myList = List.objects.get(id=pk)
    form = CreateList(instance=myList)

    if request.method == 'POST':
        form = CreateList(request.POST, instance=myList)
        if form.is_valid():
            form.save()
            return redirect('grocery_view')
        else:
            form = CreateList(instance=myList)

    return render(request, "grocery_update.html", {'form': form})


@login_required(login_url='login')
def update_item(request, pk):
    myItem = Item.objects.get(id=pk)
    form = CreateItem(instance=myItem)

    if request.method == 'POST':
        form = CreateItem(request.POST, instance=myItem)
        if form.is_valid():
            form.save()
            return redirect('grocery_view')
        else:
            form = CreateItem(instance=myItem)

    return render(request, "grocery_update.html", {'form': form})
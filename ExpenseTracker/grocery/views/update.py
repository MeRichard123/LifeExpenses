from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import CreateItem, CreateList


@login_required(login_url='login')
def update_list(request, pk):
    mylist = List.objects.get(id=pk)
    form = CreateList(instance=mylist)

    if request.method == 'POST':
        form = CreateList(request.POST, instance=mylist)
        if form.is_valid():
            form.save()
            return redirect('grocery_view')
        else:
            form = CreateList(instance=mylist)

    return render(request, "grocery_update.html", {'form': form})


@login_required(login_url='login')
def update_item(request, pk):
    myitem = Item.objects.get(id=pk)
    form = CreateItem(instance=myitem)

    if request.method == 'POST':
        form = CreateItem(request.POST, instance=myitem)
        if form.is_valid():
            form.save()
            return redirect('grocery_view')
        else:
            form = CreateItem(instance=myitem)

    return render(request, "grocery_update.html", {'form': form})
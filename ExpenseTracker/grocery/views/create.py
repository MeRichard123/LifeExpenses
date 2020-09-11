from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import CreateItem, CreateList


@login_required(login_url='login')
def create_list(request):
    form = CreateList()
    if request.method == "POST":
        form = CreateList(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            List.objects.create(
                user=request.user,
                name=name,
            )
        return redirect('grocery_view')  
    context = {'form': form}
    return render(request, "grocery_create.html", context)


@login_required(login_url='login')
def create_item(request):
    form = CreateItem()
    if request.method == "POST":
        form = CreateItem(request.POST)
        if form.is_valid():
            form.save()
        return redirect('grocery_view')
    context = {'form': form}
    return render(request, "grocery_create.html", context)

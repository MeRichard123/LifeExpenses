from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def grocery_view(request):
    items = Item.objects.all()
    myList = request.user.list.all()

    context = {
        'items': items,
        'myList': myList,
    }

    return render(request, "grocery_view.html", context)

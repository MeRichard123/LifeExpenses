from ..models import List, Item
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def grocery_view(request):
    items = Item.objects.all()
    myList = request.user.list.all()

    total_sum = 0
    for i in myList:
        for item in i.item.all():
            total_sum += item.total_item

    context = {
        'items': items,
        'myList': myList,
        'total_sum': total_sum,
    }

    return render(request, "grocery_view.html", context)

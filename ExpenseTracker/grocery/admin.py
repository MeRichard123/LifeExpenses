from django.contrib import admin
from .models import List, Item


# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']


admin.site.register(Item, ItemAdmin)
admin.site.register(List)

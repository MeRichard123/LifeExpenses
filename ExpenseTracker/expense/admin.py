from django.contrib import admin
from .models import ExpenseProfile, ExpenseItem

# Register your models here.


class ExpenseItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_purchased']
    search_fields = ['date_purchased', 'price']


admin.site.register(ExpenseItem, ExpenseItemAdmin)
admin.site.register(ExpenseProfile)

from django.contrib import admin
from .models import Category, Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'priority']
    search_fields = ['category', 'task']
    list_filter = ['category', 'priority']


admin.site.register(Category)
admin.site.register(Todo, TodoAdmin)

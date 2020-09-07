from django.contrib import admin
from .models import Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'priority', 'status']
    search_fields = ['task']


admin.site.register(Todo, TodoAdmin)


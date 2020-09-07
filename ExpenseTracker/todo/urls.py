from django.urls import path
from . import views


urlpatterns = [
    path("todo/", views.task, name="todo"),
    path("delete_task/<str:pk>", views.delete_task, name="delete_task"),
    path("create_task/", views.create_task, name="create_task"),
    path("done_task/<str:pk>", views.done_task, name="done_task"),
    path("update_task/<str:pk>", views.update_task, name="update_task"),
]

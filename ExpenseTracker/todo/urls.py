from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path("todo/", views.task, name="todo"),
    path("delete_task/<str:pk>", views.delete_task, name="delete_task"),
    path("create_task/", views.create_task, name="create_task"),
    path("done_task/<str:pk>", views.done_task, name="done_task"),
    path("update_task/<str:pk>", views.update_task, name="update_task"),
]
=======
    
]
>>>>>>> 73a66e842e2456b6653eefdd7112a3bfc3337f9d

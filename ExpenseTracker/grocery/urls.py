from django.urls import path, include
from . import views


urlpatterns = [
    path("create_list/", views.create_list, name="create_list"),
    path("create_item/", views.create_item, name="create_item"),

    path("update_list/<str:pk>", views.update_list, name="update_list"),
    path("update_item/<str:pk>", views.update_item, name="update_item"),

    path("delete_item/<str:pk>", views.delete_item, name="delete_item"),
    path("delete_list/<str:pk>", views.delete_list, name="delete_list"),

    path("grocery_view/", views.grocery_view, name="grocery_view"),
]

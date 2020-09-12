from django.contrib import admin
from django.urls import path, include
from .views import home, ExpenseList, createExpense, deleteExpense, setBudget

urlpatterns = [
    path("home/", home, name="home"),
    path("expenses/", ExpenseList, name="expense"),
    path("create_expense/", createExpense, name="create_expense"),
    path("delete_expense/<int:pk>", deleteExpense, name="remove_expense"),
    path("set_budget", setBudget, name="add_budget")
]

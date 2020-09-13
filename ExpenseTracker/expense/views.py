from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ExpenseItem, ExpenseProfile
from todo.models import Todo
from .forms import CreateExpense, AddBudget
from django.contrib import messages

# Create your views here.


@login_required(login_url="login")
def home(req):
    # Form for setting a budget limit
    budgetForm = AddBudget()
    user = req.user
    # Grab the current budget limit
    budgetProfile = ExpenseProfile.objects.filter(user=user).first()
    budget = budgetProfile.monthlyBudget
    # Get current updates
    LatestExpenses = ExpenseItem.objects.all()[:3]
    LatestTodos = Todo.objects.all().order_by("-priority")
    context = {
        'user': req.user,
        'form': budgetForm,
        'budget': budget,
        'latestExpenses': LatestExpenses,
        'latestTodos': LatestTodos,
    }
    return render(req, "dashboard.html", context)


@login_required(login_url="login")
def ExpenseList(req):
    user = req.user
    expenseList = ExpenseItem.objects.all()
    budgetProfile = ExpenseProfile.objects.filter(user=user).first()
    budget = budgetProfile.monthlyBudget
    expenseForm = CreateExpense()

    totalSum = 0
    items = user.profile.all()
    for i in items:
        for item in i.item.all():
            totalSum += item.price
    context = {
        'expenses': expenseList,
        'user': user,
        'Createform': expenseForm,
        'budget': budget,
        "sum": totalSum
    }
    return render(req, "expenses.html", context)


@login_required(login_url="login")
def createExpense(req):
    user = req.user
    userExpenseProfile = ExpenseProfile.objects.filter(user=user).first()
    if req.method == "POST":
        expenseForm = CreateExpense(req.POST)
        if expenseForm.is_valid():
            data = expenseForm.cleaned_data
            newExpense = ExpenseItem(
                userProfile=userExpenseProfile, **data)
            newExpense.save()

    return redirect("expense")


@login_required(login_url="login")
def deleteExpense(req, pk):
    user = req.user
    task = ExpenseItem.objects.get(pk=pk)
    if req.method == "POST":
        task.delete()
    return redirect("expense")


@login_required(login_url='login')
def setBudget(req):
    user = req.user
    userProfile = ExpenseProfile.objects.filter(user=user).first()
    budgetForm = AddBudget(instance=userProfile)
    if req.method == "POST":
        budgetForm = AddBudget(req.POST, instance=userProfile)
        if budgetForm.is_valid():
            budgetForm.save()

    return redirect("home")

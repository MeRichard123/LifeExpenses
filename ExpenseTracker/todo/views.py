from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateTodo
from .models import Todo
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url="login")
def task(request):
    task_form = CreateTodo()
    p_tasks = Todo.objects.filter(user=request.user).filter(status=0)
    c_tasks = Todo.objects.filter(user=request.user).filter(status=1)
    total_p_tasks = p_tasks.count()
    total_c_tasks = c_tasks.count()

    context = {
        'task_form': task_form,
        'p_tasks': p_tasks,
        'c_tasks': c_tasks,
        'total_p_tasks': total_p_tasks,
        'total_c_tasks': total_c_tasks,
    }
    return render(request, "task.html", context)


@login_required(login_url="login")
def create_task(request):
    if request.method == "POST":
        task_form = CreateTodo(request.POST)
        if task_form.is_valid():
            data = task_form.cleaned_data
            print(request.POST.get('category'))
            store = Todo(user=request.user,**data)
            store.save()
    return redirect('todo')


@login_required(login_url="login")
def delete_task(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
    return redirect('todo')


@login_required(login_url="login")
def done_task(request, pk):
    task = Todo.objects.get(id=pk)
    if request.method == "POST":
        task.status = 1
        task.save()
    return redirect('todo')


@login_required(login_url="login")
def update_task(request, pk):
    task = Todo.objects.get(id=pk)
    form = CreateTodo(instance=task)

    if request.method == "POST":
        form = CreateTodo(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            form = CreateTodo()
    return render(request, 'update.html', {"form": form})

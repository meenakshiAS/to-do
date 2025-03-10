from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from tasks.forms import TaskForm

from .models import Task


@login_required
def home(request):
    task_list = Task.objects.filter(user=request.user)
    return render(
        request, "tasks/index.html", {"title": "Home", "task_list": task_list}
    )


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks:home")
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/create_task.html",
        {"form": form, "title": "Create Task"},
    )


@login_required
def view_task(request, id):
    task_details = Task.objects.get(id=id)
    return render(request, "tasks/task.html", {"title": "Task", "task": task_details})


@login_required
def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect("tasks:home")

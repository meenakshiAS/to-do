from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from tasks.forms import TaskForm


@login_required
def home(request):
    return render(request, "tasks/index.html", {"title": "Home"})


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
from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm, NoteForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST

# Create your views here.


def task_detail(request, id):
    task_detail = get_object_or_404(Task, id=id)
    notes = task_detail.notes.all()
    form = NoteForm
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(False)
            note.task = task_detail
            note.name = request.user
            note.save()
            return redirect("task_detail", task_detail.id)
    else:
        form = NoteForm()
    context = {
        "task_detail": task_detail,
        "notes": notes,
        "form": form,
    }
    return render(request, "tasks/detail.html", context)


@login_required
def show_my_tasks(request):
    if request.method == "POST":
        # print(request.POST)
        # find task by id
        task = get_object_or_404(Task, id=request.POST["id"])
        # toggle task.is_completed
        task.is_completed = not task.is_completed
        # save task
        task.save()
        # redirect back to same route (mine)
        return redirect("show_my_tasks")
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "show_my_tasks": tasks,
    }
    return render(request, "tasks/mine.html", context)


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)

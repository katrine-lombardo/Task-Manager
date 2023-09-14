from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm, NoteForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_POST

# Create your views here.


def task_detail(request, id):
    task_detail = get_object_or_404(Task, id=id)
    notes = task_detail.notes.filter(active=True)
    form = NoteForm
    context = {
        "task_detail": task_detail,
        "notes": notes,
        "form": form,
    }
    return render(request, "tasks/detail.html", context)


# @require_POST
def note_for_task(request, id):
    task_detail = get_object_or_404(Task, id=id)
    if request.method == "POST":
        new_note = None
        note_form = NoteForm(data=request.POST)
        if note_form.is_valid():
            new_note = note_form.save(commit=False)
            new_note.task_detail = task_detail
            new_note.save()
        return redirect("tasks/note.html")
    context = {"task_detail": task_detail}
    return render(request, "tasks/detail.html", context)


@login_required
def show_my_tasks(request):
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

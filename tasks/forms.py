from django.forms import ModelForm
from tasks.models import Task, Note


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = (
            "body",
        )

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


# class CheckboxForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['is_completed', 'id']
#         widgets = {
#             'id': forms.HiddenInput(),
#             'is_completed': forms.CheckboxInput(attrs={'onclick': 'this.form.submit()'}),
#         }

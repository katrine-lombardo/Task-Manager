from django.contrib import admin
from tasks.models import Task, Note

# Register your models here.


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = [
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
    ]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'task', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'body',)
    actions = ['approve_notes']

    def approve_notes(self, request, queryset):
        queryset.update(active=True)

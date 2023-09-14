from django.urls import path
from tasks.views import create_task, show_my_tasks, task_detail, note_for_task

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("<int:id>/", task_detail, name="task_detail"),
    path("<int:id>/note/", note_for_task, name="note_for_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
]

from django.urls import path
from tasks.views import create_task, show_my_tasks, task_detail

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("<int:id>/", task_detail, name="task_detail"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
]

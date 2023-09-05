from django.shortcuts import render
from projects.models import Project

# Create your views here.


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "list_project": projects,
    }
    return render(request, "projects/list_projects.html", context)

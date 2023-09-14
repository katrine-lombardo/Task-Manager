from django.contrib import admin
from projects.models import Project, Company

# Register your models here.


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "owner",
    ]


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
    ]

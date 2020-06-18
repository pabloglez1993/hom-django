from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Project
from django.db.models import Sum

@login_required
def list_projects(request):
    Projects = Project.objects.annotate(
        sum_estimated_price=Sum('task__concept__estimated_price'),
        sum_real_price=Sum('task__concept__real_price')
    )
    return render(request, 'projects/list.html', {'projects': Projects})

@login_required
def add_project(request):
    return render(request, 'projects/add_project.html')
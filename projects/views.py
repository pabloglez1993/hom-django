from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from projects.models import Project, Owner, Task, Concept
from users.models import Architect
from django.db.models import Sum, Max, Min
from datetime import datetime, timedelta

from projects.forms import ProjectForm,TaskForm

@login_required
def list_projects(request):
    if 'search' in request.GET:
        projects = Project.objects.annotate(
            sum_estimated_price=Sum('task__concept__estimated_price'),
            sum_real_price=Sum('task__concept__real_price'),
        ).filter(name__icontains=request.GET['search'])
    else:    
        projects = Project.objects.annotate(
            sum_estimated_price=Sum('task__concept__estimated_price'),
            sum_real_price=Sum('task__concept__real_price'),
        )
        
    return render(request, 'projects/list.html', {'projects': projects})

@login_required
def add_project(request):
    architects = Architect.objects.values('architect__username', 'id')
    owners = Owner.objects.values('first_name', 'last_name', 'id')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()

    return render(
        request, 
        'projects/add_project.html',
        {
            'form': form, 
            'architects': architects,
            'owners': owners,
            'types': Project.BUILDING_TYPES
        }
    )

@login_required
def edit_project(request, id):
    project = Project.objects.get(id=id)
    architects = Architect.objects.values('architect__username', 'id')
    owners = Owner.objects.values('first_name', 'last_name', 'id')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            project.architect = data['architect']
            project.owner = data['owner']
            project.name = data['name']
            project.area = data['area']
            project.type = data['type']
            project.start_date = data['start_date']
            project.end_date = data['end_date']
            project.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()

    return render(
        request, 
        'projects/edit_project.html', 
        {
            'project': project, 
            'form': form, 
            'architects': architects,
            'owners': owners,
            'types': Project.BUILDING_TYPES
        }
    )
    
@login_required
def delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect('list_projects')

@login_required
def list_tasks(request, id):
    project = Project.objects.get(pk=id)
    tasks = Task.objects.filter(project=id).order_by('start_date')

    monday1 = (project.start_date - timedelta(days=project.start_date.weekday()))
    monday2 = (project.end_date - timedelta(days=project.end_date.weekday()))
    weeks_project = int((monday2 - monday1).days / 7)
    
    tasks_detail = {}
    previous_week_len = 0

    for task in tasks:
        monday1 = (task.start_date - timedelta(days=task.start_date.weekday()))
        monday2 = (task.end_date - timedelta(days=task.end_date.weekday()))
        weeks_task = int((monday2 - monday1).days / 7)
        tasks_detail[task.name] = [
            Concept.objects.filter(task=task.id).values('description', 'id'),
            weeks_task,
            previous_week_len,
        ]
        previous_week_len += weeks_task

    return render(
        request, 
        'calendar/list_tasks.html',
        {
            'project': project,
            'weeks_project': range(1, weeks_project),
            'tasks_detail': tasks_detail
        }
    )

@login_required
def add_task(request,id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['project'] = project
            if not Task.objects.filter(project=project, name=data['name']).__len__():
                Task.objects.create(**data)
            else:
                messages.add_message(request, messages.WARNING, 'YA EXISTE.')
            return redirect('list_tasks/')
        else:
            print('NOT VALID')
    else:
        form = TaskForm()

    return render(
        request, 
        'calendar/add_task.html',
        {
            'id': id,
            'form': form, 
        }
    )

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('list_task')


@login_required
def edit_task(request, project_id, task_id):
    project = Project.objects.get(pk=project_id)
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.project = project_id
            task.name = data['name']
            task.start_date = data['start_date']
            task.end_date = data['end_date']
            project.save()
            return redirect('list_task/')
    else:
        form = TaskForm()

    return render(
        request, 
        'calendar/edit_task.html', 
        {
            'task':task,
            'project': project, 
            'form': form, 
            'architects': architects,
            'owners': owners,
            'types': Project.BUILDING_TYPES
        }
    )
import math

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from projects.models import Project, Owner, Task, Concept
from users.models import Architect
from django.db.models import Sum, Max, Min
from datetime import datetime, timedelta

from projects.forms import ProjectForm,TaskForm,ConceptForm

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
    project = Project.objects.get(pk=id)
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
    
    weeks_dates = list()
    week = 0
    for i in range(weeks_project):
        weeks_dates.append(monday1 + timedelta(days=week))
        week += 7
    
    tasks_detail = dict()
    previous_week = 0
    
    for task in tasks:
        monday1 = (task.start_date - timedelta(days=task.start_date.weekday()))
        monday2 = (task.end_date - timedelta(days=task.end_date.weekday()))
        if previous_week == 0:
            previous_date = 0
        else:
            previous_date = math.floor((task.start_date - previous_date).days / 7)
            
        weeks_task = math.ceil((task.end_date - task.start_date).days / 7) + 1
        task_id = int(task.id)
        tasks_detail[task.name] = [
            Concept.objects.filter(task=task.id).values('description', 'id'), 
            weeks_task,
            #previous_week,
            previous_date,
            task_id,
            Concept.objects.filter(task=task.id).values('description', 'id', 'estimated_volume', 'estimated_price', 'unit', 'real_volume', 'real_price') 
        ]   
        previous_week += weeks_task
        previous_date = task.start_date

    return render(
        request, 
        'calendar/list_tasks.html',
        {
            'project': project,
            #'weeks_project': range(1, weeks_project),
            'weeks_project': weeks_dates,
            'tasks_detail': tasks_detail,
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
            return redirect('list_tasks',id)
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
    
@login_required
def delete_task(request, id, id2):
    tasks = Task.objects.filter(project=id2).order_by('start_date')
    #import pdb; pdb.set_trace()
    for n in tasks:
        if n.pk == id:
            tarea_a_borrar = n
    tarea_a_borrar.delete()
    return redirect('list_tasks',id2)


@login_required
def edit_task(request, id, id2):
    project = Project.objects.get(pk= id2)
    task = Task.objects.get(pk= id, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['project'] = project
            Task.objects.filter(pk=id, project=data['project']).update(**data)
            return redirect('list_tasks',id2)
    else:
        form = TaskForm()

    return render(
        request, 
        'calendar/edit_task.html', 
        {
            'task':task,
            'project': project, 
            'form': form, 
            'messages': messages
        }
    )

@login_required
def add_concept(request, id, id2):
    project = Project.objects.get(pk= id)
    tasks = Task.objects.filter(project=project).order_by('start_date')
    for n in tasks:
        if n.pk == id2:
            task = n

    if request.method == 'POST':
        form = ConceptForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['task'] = task
            if not Task.objects.filter(project=project, name=data['description']).__len__():
                Concept.objects.create(**data)
            else:
                messages.add_message(request, messages.WARNING, 'YA EXISTE.')
            return redirect('list_tasks',id)
    else:
        form = TaskForm()

    return render(
        request, 
        'calendar/add_concept.html',
        {
            'task': task,
            'project': project,
            'form': form,
            'message': messages 
        }
    )

@login_required
def edit_concepto(request,id,id2,id3):

    project = Project.objects.get(pk= id2)
    task = Task.objects.get(pk= id, project=project) 
    concept = Concept.objects.get(pk= id3, task=task)
    if request.method == 'POST':
        form = ConceptForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['task'] = task
            Concept.objects.filter(pk=id3, task=task).update(**data)
            return redirect('list_tasks',id2)
    else:
        form = ConceptForm()

    return render(
        request, 
        'calendar/edit_concepto.html', 
        {
            'task':task,
            'project': project, 
            'form': form, 
            'concept': concept,
        }
    )

@login_required
def delete_concepto(request,id,id2,id3):
    
    project = Project.objects.get(pk= id2)
    task = Task.objects.get(pk = id, project=project)
    concept = Concept.objects.get(pk = id3, task=task)
    concept.delete()
    return redirect('list_tasks',id2)   
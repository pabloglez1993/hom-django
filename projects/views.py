from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from projects.models import Project, Owner
from users.models import Architect
from django.db.models import Sum

from projects.forms import ProjectForm

@login_required
def list_projects(request):
    if request.GET:
        Projects = Project.objects.annotate(
            sum_estimated_price=Sum('task__concept__estimated_price'),
            sum_real_price=Sum('task__concept__real_price')
        ).filter(name__icontains=request.GET['search'])
    else:    
        Projects = Project.objects.annotate(
            sum_estimated_price=Sum('task__concept__estimated_price'),
            sum_real_price=Sum('task__concept__real_price')
        )
        
    return render(request, 'projects/list.html', {'projects': Projects})

@login_required
def add_project(request):
    architects = Architect.objects.values('architect__username')
    owners = Owner.objects.values('first_name')
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            project = Project(
                architect=data['architect'],
                owner=data['owner'],
                name=data['name'],
                area=data['area'],
                type=data['type'],
                start_date=data['start_date'],
                end_date=data['end_date']
            )
            project.save()
            
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
    architects = Architect.objects.values('architect__username')
    owners = Owner.objects.values('first_name')
    
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
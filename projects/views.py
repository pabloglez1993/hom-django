from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from projects.models import Project, Owner
from users.models import Architect
from django.db.models import Sum

from projects.forms import ProjectForm

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

@login_required
def edit_project(request, id):
    projectSave = Project.objects.get(pk=id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            projectSave.architect = data['architect']
            projectSave.owner = data['owner']
            projectSave.name = data['name']
            projectSave.area = data['area']
            projectSave.type = data['type']
            projectSave.start_date = data['start_date']
            projectSave.end_date = data['end_date']
            projectSave.save()
            
            return redirect('list_projects')
    else:
        form = ProjectForm()
    project = Project.objects.get(pk=id)
    architects = Architect.objects.values('architect__username')
    owners = Owner.objects.values('first_name')
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
from django.shortcuts import render

projects = [
    {
        'name': 'P1',
        'owner': 'Pablo'
    },
    {
        'name': 'P2',
        'owner': 'Felipe'
    },
]

def list_projects(request):
    return render(request, 'projects.html', {'projects': projects})
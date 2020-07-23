from django import forms
from projects.models import Project,Task,Concept

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('architect', 'owner', 'name', 'area', 'type', 'start_date', 'end_date',)
        
#voy a agregar una clase TaskForm para seguir tu sintaxis en las views porfavor revisa si esta bien

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name','start_date','end_date',)

class ConceptForm(forms.ModelForm):
    class Meta:
        model = Concept
        fields = ('description','estimated_volume','estimated_price','unit','real_volume','real_price',)

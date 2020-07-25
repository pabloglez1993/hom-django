from django import forms
from projects.models import Project,Task,Concept
from datetime import datetime

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('architect', 'owner', 'name', 'area', 'type', 'start_date', 'end_date',)
        
    def clean_start_date(self):
        sd = self.data['start_date']
        ed = self.data['end_date']
        if sd == '':
            raise forms.ValidationError("Start date needs a value")
        if sd >= ed:
            raise forms.ValidationError("Start date greater than end date")
        return sd
    
    def clean_end_date(self):
        ed = self.data['end_date']
        if ed == '':
            raise forms.ValidationError("End date needs a value")
        return ed
        
#voy a agregar una clase TaskForm para seguir tu sintaxis en las views porfavor revisa si esta bien

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name','start_date','end_date',)
        
    # def clean_project(self):
    #     project = self.data['project']
    #     sd = self.data['start_date']
    #     ed = self.data['end_date']
        
    #     if project.start_date <= sd and project.end_date >= ed:
    #         raise forms.ValidationError("Task dates out of range")
    #     return project
    
    def clean_start_date(self):
        sd = self.data['start_date']
        ed = self.data['end_date']
        if sd == '':
            raise forms.ValidationError("Start date needs a value")
        if sd >= ed:
            raise forms.ValidationError("Start date greater than end date")
        return sd
    
    def clean_end_date(self):
        ed = self.data['end_date']
        if ed == '':
            raise forms.ValidationError("End date needs a value")
        return ed

class ConceptForm(forms.ModelForm):
    class Meta:
        model = Concept
        fields = ('description','estimated_volume','estimated_price','unit','real_volume','real_price',)

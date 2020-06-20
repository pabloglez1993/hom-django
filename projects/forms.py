from django import forms
from users.models import Architect
from projects.models import Owner, Project

class ProjectForm(forms.Form):
    architect = forms.ModelChoiceField(queryset=Architect.objects.all(), to_field_name='architect__username')
    owner = forms.ModelChoiceField(queryset=Owner.objects.all(), to_field_name='first_name')
    name = forms.CharField(max_length=50, required=True)
    area = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    type = forms.ChoiceField(choices=Project.BUILDING_TYPES)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
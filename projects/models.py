from django.db import models

from users.models import Architect

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Project(models.Model):
    BUILDING_TYPES = [
        ('Department', 'Department'),
        ('House', 'House'),
        ('Building', 'Building'),
        ('Reparation', 'Reparation'),
        ('Other', 'Other'),
    ]
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=10, choices=BUILDING_TYPES, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.project} - {self.name}'

class Concept(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField()
    estimated_volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    estimated_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    real_volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    real_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return f'{self.task} - {self.description}'
from django.contrib import admin

from .models import Owner, Project, Task, Concept
    
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cell_phone')
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'architect', 'owner', 'start_date', 'end_date')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'start_date', 'end_date')
    
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('description', 'task', 'estimated_volume', 'estimated_price', 'unit')

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Concept, ConceptAdmin)

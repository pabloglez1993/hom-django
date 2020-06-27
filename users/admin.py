from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from users.models import Architect


class ArchitectAdmin(admin.ModelAdmin):
    list_display = ('architect', 'cell_phone',)
    #list_display_links = ()
    #list_editable = ('cell_phone',)
    search_fields = (
        'architect__username', 
        'architect__first_name', 
        'architect__last_name', 
        'cell_phone'
    )
    fieldsets = (
        ('Required Info', {
            "fields": (
                ('architect', 'cell_phone',),
            ),
        }),
    )
    
class ArchitectInline(admin.StackedInline):
    model = Architect
    can_delete = False
    
class ArchitectAdmin(UserAdmin):
    inlines = (ArchitectInline,)
    
admin.site.unregister(User)
admin.site.register(User, ArchitectAdmin)
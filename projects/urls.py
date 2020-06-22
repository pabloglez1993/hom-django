from django.urls import path

from projects import views
#import pdb; pdb.set_trace()

urlpatterns = [
    path('', views.list_projects, name='list_projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
    path('calendar/<int:id>', views.list_tasks, name='list_tasks'),
]
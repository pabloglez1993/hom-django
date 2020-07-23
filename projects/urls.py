from django.urls import path

from projects import views
#import pdb; pdb.set_trace()

urlpatterns = [
    #project urls
    path('', views.list_projects, name='list_projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
    #task urls
    path('calendar/<int:id>', views.list_tasks, name='list_tasks'),
    path('calendar/<int:id>/add_task/', views.add_task, name='add_task'),
    path('calendar/<int:id>/<int:id2>delete_task/', views.delete_task, name='delete_task'),
    path('calendar/<int:id>/<int:id2>edit_task/', views.edit_task, name='edit_task'),
    #Concept urls
    path('calendar/<int:id>/<int:id2>/add_concept', views.add_concept, name='add_concept'),
    path('calendar/<int:id>/<int:id2>/<int:id3>/edit_concepto', views.edit_concepto, name='edit_concepto'),
    path('calendar/<int:id>/<int:id2>/<int:id3>/delete_concepto', views.delete_concepto, name='delete_concepto'),
]
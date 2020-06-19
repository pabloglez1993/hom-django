from django.urls import path

from projects import views
#import pdb; pdb.set_trace()

urlpatterns = [
    path('', views.list_projects, name='list_projects'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:id>', views.edit_project, name='edit_project'),
]
from django.urls import path

from projects import views
#import pdb; pdb.set_trace()

urlpatterns = [
    path('', views.list_projects),
]
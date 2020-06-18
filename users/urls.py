from django.urls import path

from users import views
#import pdb; pdb.set_trace()

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
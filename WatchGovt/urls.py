from django.urls import path
from .views import register, login_view, project_list, create_project

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('projects/', project_list, name='project_list'),
    path('projects/create/', create_project, name='create_project'),
]

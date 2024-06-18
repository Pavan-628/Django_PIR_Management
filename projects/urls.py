from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projects', views.project_list, name='project_list'),
    path('profile/', views.profile, name='profile'),  # Add this line
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    #path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('projects/new/', views.new_project, name='new_project'),
]

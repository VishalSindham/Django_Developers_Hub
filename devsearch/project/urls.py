from django.urls import path
from . import views

urlpatterns = [

    path('', views.projects, name='projects'),
    path('create-project/',views.createProject, name='create-project'),
    path('single/<str:pk>/',views.single_project, name='single_project'),
    path('update/<str:pk>/',views.updateProject, name='update_project'),
    path('delete/<str:pk>/', views.deleteProject, name='delete_project'),

]
from django.urls import path,include 
from .import views 
from django.contrib.auth import views as auth_views 
urlpatterns = [ 
    path('tasks/', views.task_list, name='task_list'), 
    path('task/create/', views.task_create, name='task_create'), 
    path('task/<int:task_id>/', views.task_detail, name='task_detail'), 
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'), 
    path('task/<int:task_id>/mark_completed', views.task_mark_complete, name='task_mark_complete'), 
    path('task/register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='task/login.html'), name='login'),                                                                                                                 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    ]
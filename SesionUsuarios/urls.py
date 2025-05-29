from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-login/', views.register_login, name='register_login'), 
    path('logout/', views.cerrar_sesion, name='logout'), 
    path('tasks/', views.tasks, name='tasks'),  
]
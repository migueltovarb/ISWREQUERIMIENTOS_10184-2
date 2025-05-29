from django.urls import path 
from . import views

urlpatterns = [
    path('nuevo/', views.registrar_reclamo, name='registrar_reclamo'),
    path('estado/', views.ver_estado_reclamo, name='ver_estado_reclamo'),
    ]


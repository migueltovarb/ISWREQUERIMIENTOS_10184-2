from django.urls import path
from . import views

urlpatterns = [
    path('nuevo/', views.registrar_solicitud, name='registrar_solicitud'),
]

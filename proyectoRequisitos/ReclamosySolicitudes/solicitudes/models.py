from django.db import models

# Create your models here.

class Solicitud(models.Model):

    CATEGORIAS = [
        ('Facturación', 'Facturación'),
        ('Daños', 'Daños'),
        ('Servicio interrumpido', 'Servicio interrumpido'),
        ('Atención al cliente', 'Atención al cliente'),
        ('Otro', 'Otro'),
    ]

    titulo = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    celular = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=500)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    def __str__(self):
        return f'Solicitud de {self.titulo}'

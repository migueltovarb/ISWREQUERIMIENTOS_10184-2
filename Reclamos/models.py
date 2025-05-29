from django.db import models
import uuid

# Create your models here.
class Reclamo(models.Model):

    CATEGORIAS = [
        ('Facturación', 'Facturación'),
        ('Daños', 'Daños'),
        ('Servicio interrumpido', 'Servicio interrumpido'),
        ('Atención al cliente', 'Atencion al cliente'),
        ('Otro','Otro'),

    ]

    TICKET_STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
    ]

    titulo = models.CharField(max_length = 50 )
    correo = models.EmailField(max_length = 100)
    celular = models.CharField(max_length = 10)
    descripcion = models.TextField(max_length = 500 )
    categoria = models.CharField(max_length = 30, choices = CATEGORIAS)
    evidencia = models.FileField(upload_to = 'evidencias/',blank = True,null = True)
    ticket = models.CharField(max_length = 10, unique = True,editable = False, default=uuid.uuid4)
    fecha = models.DateTimeField(auto_now_add = True)
    estado = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='pendiente')

    def __str__(self):
        return f'Reclamo {self.ticket} - {self.titulo}'

    def get_estado(self):
        return dict(self.TICKET_STATUS_CHOICES).get(self.estado, self.estado)
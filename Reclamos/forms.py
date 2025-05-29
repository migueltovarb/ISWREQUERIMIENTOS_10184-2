from django import forms
from .models import Reclamo

class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['titulo', 'correo','celular','descripcion','categoria','evidencia']

        widgets = {

            'titulo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'maxlength': 500}),
            'categoria': forms.Select(choices = [
                        ('Facturación', 'Facturación'),
                        ('Daños', 'Daños'),
                        ('Servicio interrumpido', 'Servicio interrumpido'),
                        ('Atención al cliente', 'Atencion al cliente'),
                        ('Otro','Otro'),
            ], attrs = {'class': 'form-control'}),
            'evidencia': forms.ClearableFileInput(attrs = {'class': 'form-control'}),

        }
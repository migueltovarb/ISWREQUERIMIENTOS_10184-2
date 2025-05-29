from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs = {'rows': 4})
        }
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Contraseña',
            'autocomplete': 'new-password'
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input-field',
            'placeholder': 'Confirmar contraseña',
            'autocomplete': 'new-password'
        })
    )

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Nombre de usuario',
                'autocomplete': 'username'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        if password and password2 and password != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return cleaned_data

    def save(self, commit=True):
        """Crear el usuario con la contraseña correctamente seteada."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

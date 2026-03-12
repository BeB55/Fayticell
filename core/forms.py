from django import forms
from django.contrib.auth.models import User
from .models import Profile, Producto

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['telefono']
        widgets = {
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de teléfono'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', "descripcion", 'precio', 'categoria', 'imagen', "destacado"]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'destacado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

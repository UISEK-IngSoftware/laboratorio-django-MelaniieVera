from django import forms
from .models import Pokemon
from .models import Entrenador

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'type', 'weight', 'height', 'picture', 'entrenador']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Charmander'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fuego'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id' : 'image_field',
            }),
            'entrenador': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'entrenador': 'Asignar a Entrenador',
        }

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['name', 'lastname', 'level', 'picture']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ash'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ketchum'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id' : 'image_field',
            }),
        }
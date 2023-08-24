from django import forms
from .models import jugador, entrenador, Equipo, Partido

class JugadorForm(forms.ModelForm):
    class Meta:
        model = jugador
        fields = ['nombre', 'apellido', 'edad', 'posicion', 'nacionalidad', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'posicion': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = entrenador
        fields = ['nombre', 'apellido', 'edad', 'nacionalidad', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'ciudad', 'entrenador', 'jugadores']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'entrenador': forms.Select(attrs={'class': 'form-control'}),
            'jugadores': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['fecha', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
            'equipo_local': forms.Select(attrs={'class': 'form-control'}),
            'equipo_visitante': forms.Select(attrs={'class': 'form-control'}),
            'goles_local': forms.NumberInput(attrs={'class': 'form-control'}),
            'goles_visitante': forms.NumberInput(attrs={'class': 'form-control'}),
        }
from django.forms import ModelForm
from django import forms
from equipos.models import Equipo

class EquiposForm(ModelForm):
    imei = forms.CharField(required=False)

    class Meta:
        model = Equipo
        fields = ['imei']

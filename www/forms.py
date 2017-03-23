from django import forms
from .models import Runner, Category, Time, Metas, Competition
from django.db import models

class RunnerForm(forms.ModelForm):
    class Meta:
        model = Runner
        fields = ['first_name', 'last_name', 'birtday',
                  'category', 'distance', 'image']
#'metas'
class MetasForm(forms.ModelForm):
    class Meta:
      model = Metas
      fields = ['meta']


class LoginForm(forms.Form):
    username = forms.CharField(label = 'User Name', max_length = 64)
    password = forms.CharField(widget = forms.PasswordInput())


class CompeForm(forms.ModelForm):
    class Meta:
      model = Time
      fields = ['time', 'distance', 'compentition']


class CompetenciaForm(forms.ModelForm):
    class Meta:
      model = Competition
      fields = ['name', 'place', 'weather', 'date']


class CategoriaForm(forms.ModelForm):
    class Meta:
      model = Category
      fields = ['name', 'first_year', 'secon_year']

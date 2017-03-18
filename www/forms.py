from django import forms
from .models import Runner, Category, Time, Metas

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

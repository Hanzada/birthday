from django import forms
from .models import Tost
class TostForm(forms.ModelForm):
    class Meta:
        model=Tost
        fields = ['avtor', 'text']
        widgets = {
            'avtor': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }

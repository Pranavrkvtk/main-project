from django import forms
from .models import news
class Newsform(forms.ModelForm):
    class Meta:
        model=news
        fields="__all__"

from django import forms
from firstapp import models
class musician_form(forms.ModelForm):
    class Meta:
        model=models.musician
        fields="__all__"


class album_form(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=models.album
        fields="__all__"
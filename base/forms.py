from django.forms import ModelForm
from django import forms
from .models import Item

class UploadForm(ModelForm):
    name = forms.TextInput()
    birth = forms.DateInput()
    class Meta:
        model = Item
        fields = ['name', 'birth']
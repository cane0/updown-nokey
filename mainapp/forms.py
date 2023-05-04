from django import forms
from .models import *
from django.shortcuts import render

class UpImgForm(forms.ModelForm):
    class Meta:
        model = UpImg
        fields = ['name', 'up_img']
# forms.py
from django import forms
from .models import *


class Profile_webForm(forms.ModelForm):

    class Meta:
        model = Profile_web
        fields = ['profile_Main_Img']

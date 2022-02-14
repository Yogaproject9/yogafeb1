from django import forms

from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image',
        ]
        widgets = {
           'profile_image': forms.FileInput(attrs={'capture': 'camera'}),

        }
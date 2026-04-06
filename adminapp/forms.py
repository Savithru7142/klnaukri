from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model= Useraccount
        fields=['firstname', 'lastname', 'email', 'phonenumber', 'role', 'password']
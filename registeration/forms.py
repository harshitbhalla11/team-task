from django import forms
from .models import TeamUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TeamUser
        fields = ["username", "email", "password"]

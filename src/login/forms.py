from django import forms
from login.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", )
        widgets = {'username': forms.fields.TextInput(attrs={'placeholder': "Nom d'utilisateur"}),
                   'Password': forms.fields.TextInput(attrs={'placeholder': "Mot de passe"}),
                   'Password confirmation': forms.fields.TextInput(attrs={'placeholder': "Confirmez mot de passe"})}


from django import forms
from login.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", )
        


from login.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        labels = {"username": "Nom d'utilisateur",
                  "password": "Mot de passe",
                  "password confirmation" : "Confirmez le mot de passe"}


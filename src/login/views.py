from django.shortcuts import redirect, render
from login.forms import UserRegistrationForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()

    return render(request, "login/signup.html", {"form" : form})

from django.shortcuts import render, redirect
from .forms import UserRegister
from django.contrib import messages
from .decorators import authenticated_user


# Create your views here.


def register(request):
    if request.method == "POST":
        Form = UserRegister(request.POST)
        # UserCreation and validation comes from django
        if Form.is_valid():
            Form.save()  # save user and hash password
            username = Form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created. You can now log in")
            return redirect("login")

    else:
        Form = UserRegister()
    return render(request, "register.html", {'form': Form})


@authenticated_user
def landing(req):
    return render(req, "landing.html")

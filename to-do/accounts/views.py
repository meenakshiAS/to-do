from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render

from .forms import RegisterUserForm


def register(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        try:
            # We need to do error handling in case the email already exist
            if form.is_valid():
                # Check if the form is valid before we save
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get("email")
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                password1 = form.cleaned_data.get("password1")
                user = User(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.set_password(password1)
                user.save()
                # Inform the user form was saved successfully.
                messages.success(request, "New user was created successfully")
                return redirect("accounts:login")
        except IntegrityError:
            messages.error(request, "The email has already been registered.")
    return render(
        request, "accounts/register.html", {"title": "register", "form": form}
    )

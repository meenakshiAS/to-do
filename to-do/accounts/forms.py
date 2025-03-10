from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "username",
            }
        ),
    )
    password = forms.CharField(
        max_length=100,
        label="Password",
        help_text="Enter password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "password", "placeholder": "Password"}
        ),
    )

    class Meta:
        """Model and field information"""

        model = User
        fields = ["username", "password"]


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        label="Username:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Username:",
            }
        ),
    )
    email = forms.CharField(
        max_length=100,
        label="Email:",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Email address",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=100,
        label="First Name:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name",
                "placeholder": "First Name:",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        label="Last Name:",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "last_name",
                "placeholder": "Last Name:",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=100,
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password1",
                "placeholder": "Enter Password:",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=100,
        label="Confirm Password:",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password2",
                "placeholder": "Confirm Password:",
            }
        ),
    )

    class Meta:
        """User Model"""

        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def clean_password(self):
        """Password validation"""
        password1 = self.cleaned_data.get("passord1")
        password2 = self.cleaned_data.get("passord2")

        if password1 != password2:
            raise ValidationError("The two passwords do not match!")
        else:
            password_validation.validate_password(password1)
            return password1

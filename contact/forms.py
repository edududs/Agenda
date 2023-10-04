from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(widget=forms.FileInput(attrs={"acept": "image/*"}))

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            msg = ValidationError(
                "Nome e sobrenome precisam ser diferentes", code="invalid"
            )
            self.add_error("first_name", msg)
            self.add_error("last_name", msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name == "boceta":
            msg = ValidationError("Nome inadequado", code="invalid")
            self.add_error("first_name", msg)
            return first_name
        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, required=True)
    last_name = forms.CharField(min_length=3, required=True)
    email = forms.EmailField(min_length=3, required=True)
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            msg = ValidationError("Email já cadastrado", code="invalid")
            self.add_error("email", msg)
        return email

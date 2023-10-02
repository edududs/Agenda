from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Esse placeholder veio do forms.py",
            }
        ),
        label="Primeiro Nome",
        help_text="Seu primeiro nome",
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Esse placeholder veio do forms.py",
            }
        ),
        label="Sobrenome",
        help_text="Seu sobrenome",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
        )

        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Nome"}
        #     ),
        #     "last_name": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Sobrenome"}
        #     ),
        #     "phone": forms.NumberInput(
        #         attrs={"class": "form-control", "placeholder": "(XX)XXXXX-XXXX"}
        #     ),
        #     "email": forms.EmailInput(
        #         attrs={"class": "form-control", "placeholder": "Email"}
        #     ),
        # }

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

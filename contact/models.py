from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
# id (primary key - automático)
# first_name (string), last_name (string), phone(string)
# email(email), created_date (date), description (text)
# category (foreing key), show (boolean), owner (foreing_key)
# picture (imagem)


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField("Category", max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Contact(models.Model):
    first_name = models.CharField("First Name", max_length=255)
    last_name = models.CharField("Last Name", max_length=255, blank=True)
    phone = models.CharField("Phone", max_length=14)
    email = models.EmailField("E-mail", max_length=255, blank=True)
    created_date = models.DateTimeField("Created Data", default=timezone.now)
    description = models.TextField("Description", blank=True)
    show = models.BooleanField("Show", default=True)
    picture = models.ImageField("Picture", upload_to="pictures/%Y/%m", blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

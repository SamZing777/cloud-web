from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class User(AbstractUser):
    country: str = CountryField(blank_label="(select country)", multiple=True)

    def __str__(self):
        return self.username

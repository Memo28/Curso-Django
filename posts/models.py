#For the ORM
from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True, default='Something cool here')
    birthdate = models.DateField(blank=True, null=True)

    country = models.TextField(blank=True)
    city = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


def __str_(self):
    return self.email
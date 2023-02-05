from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').null = False

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
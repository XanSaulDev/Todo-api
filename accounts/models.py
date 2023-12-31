from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name','last_name']
  objects = UserManager()

  def __str__(self):
    return self.get_full_name()
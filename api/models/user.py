from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

from .base_model import BaseModel


class User(BaseModel, AbstractBaseUser):
    auth0_id = models.TextField(unique=True)
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()

    USERNAME_FIELD = 'auth0_id'
    EMAIL_FIELD = 'email'
    password = None
    last_login = None

    objects = UserManager()

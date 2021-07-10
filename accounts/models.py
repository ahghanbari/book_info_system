from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import BaseUserManager


class CustomUser(AbstractUser):
    username = models.EmailField('Email address', max_length=255, unique=True, db_index=True)
    full_name = models.CharField(('full name'), max_length=150, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']


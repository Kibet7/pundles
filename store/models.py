# store/models.py
from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser (AbstractUser ):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    # Additional fields can be added as needed
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    limit = models.IntegerField(default=0) 
    # add additional fields in here
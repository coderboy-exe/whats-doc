from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

class User(AbstractUser):
    """User class white inherits from contrib User model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
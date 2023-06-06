from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.

class User(AbstractUser):
    """User class which inherits from contrib User model"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # profile_pic = models.ImageField(upload)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_as_doctor')
#     scheduled_time = models.DateTimeField()
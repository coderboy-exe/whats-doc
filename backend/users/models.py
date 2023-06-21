from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from datetime import datetime
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


TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    scheduled_time = models.DateTimeField(default=datetime.now)
    time_choice = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    meeting_link = models.TextField(default='')
    name = models.TextField(default='')
    description = models.TextField(default='')
    
    def __str__(self):
        return f"Name: {self.name} | User: {self.user.username} | Doctor: {self.doctor.username} | Scheduled Time: {self.time_choice} | Link: {self.meeting_link}"

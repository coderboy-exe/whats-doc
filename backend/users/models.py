from django.db import models
from django.contrib.auth.models import AbstractUser

import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import io

from uuid import uuid4
from datetime import datetime
from datetime import date
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
    scheduled_time = models.CharField(default='3 PM', max_length=10)
    date_choice = models.DateField(default=date.today)
    meeting_link = models.TextField(default='')
    name = models.TextField(default='')
    description = models.TextField(default='')
    
    def __str__(self):
        return f"Name: {self.name} | User: {self.user.username} | Doctor: {self.doctor.username} | Scheduled Time: {self.time_choice} | Link: {self.meeting_link}"


class HealthRecords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')
    title = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    prescription = models.TextField(default='')
    attachment = models.ImageField(upload_to='health_records/', blank=True)

    def compress_image(self):
        if self.attachment:
            img = Image.open(self.attachment)
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.attachment = InMemoryUploadedFile(output, 'ImageField', f'{self.attachment.name.split(".")[0]}.jpg', 'image/jpeg', sys.getsizeof(output), None)
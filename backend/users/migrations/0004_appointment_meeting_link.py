# Generated by Django 4.1.7 on 2023-06-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_appointment_scheduled_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='meeting_link',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-21 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_healthrecords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time_choice',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_choice',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.CharField(default='3 PM', max_length=10),
        ),
    ]

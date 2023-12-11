from django.db import models
from django.utils import timezone

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)


class Messages(models.Model):
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now)

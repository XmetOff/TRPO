from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from chat_room.models import Room


# Create your models here.

class Message(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    room = models.ForeignKey(Room)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

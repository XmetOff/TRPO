from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from chat_room.models import Chat


class ChatMessage(models.Model):
    author = models.ForeignKey(User)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    chat = models.ForeignKey(Chat)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

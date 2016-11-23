from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

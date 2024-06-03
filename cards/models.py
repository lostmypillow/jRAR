from django.db import models
from django.utils import timezone


class Card(models.Model):
    card_val = models.CharField(max_length=200)



class RequestAttempt(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    successful = models.BooleanField()

    def __str__(self):
        return f"RequestAttempt(successful={self.successful}, timestamp={self.timestamp})"

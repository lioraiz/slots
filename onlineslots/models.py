from django.contrib.auth.models import User
from django.db import models

# The funds table
class Funds(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=100)

    def __str__(self):
        return str(self.player)

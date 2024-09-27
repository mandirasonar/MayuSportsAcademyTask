# players/models.py
from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Player(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


# players/models.py
class Coach(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      team = models.CharField(max_length=50)

      def __str__(self):
        return f"{self.user.username} - {self.team}"

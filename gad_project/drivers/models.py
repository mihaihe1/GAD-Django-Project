from django.db import models
from teams.models import Team


class Driver(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    podiums = models.PositiveIntegerField()
    highest_race_finish = models.PositiveIntegerField(default=4)
    age = models.PositiveIntegerField()
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

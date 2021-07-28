from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    power_unit = models.CharField(max_length=30)
    world_championships = models.PositiveIntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Driver(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    podiums = models.PositiveIntegerField()
    highest_race_finish = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

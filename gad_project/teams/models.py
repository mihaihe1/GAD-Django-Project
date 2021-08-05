from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30)
    power_unit = models.CharField(max_length=30)
    world_championships = models.PositiveIntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name

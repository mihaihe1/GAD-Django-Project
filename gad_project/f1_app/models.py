from django.db import models
from datetime import datetime


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Team(MyModel):
    name = models.CharField(max_length=30)
    power_unit = models.CharField(max_length=30)
    world_championships = models.PositiveIntegerField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pilot(MyModel):
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


class Circuit(MyModel):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    capacity = models.DecimalField(max_digits=6, decimal_places=3)
    gps_held = models.PositiveIntegerField()
    length = models.DecimalField(max_digits=4, decimal_places=3)
    lap_record = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Race(MyModel):
    name = models.CharField(max_length=50)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    first_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='first_place')
    second_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='second_place')
    third_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='third_place')
    date = models.DateTimeField()
    sold_out = models.BooleanField()

    def __str__(self):
        return self.name


from django.db import models


class Circuit(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    capacity = models.DecimalField(max_digits=6, decimal_places=3)
    gps_held = models.PositiveIntegerField()
    length = models.DecimalField(max_digits=4, decimal_places=3)
    lap_record = models.CharField(max_length=30)

    def __str__(self):
        return self.name

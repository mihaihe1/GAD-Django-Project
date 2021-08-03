from django.db import models
from drivers.models import Driver
from circuits.models import Circuit


class Race(models.Model):
    name = models.CharField(max_length=50)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    first_place = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='first_place')
    second_place = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='second_place')
    third_place = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='third_place')
    date = models.DateTimeField()
    sold_out = models.BooleanField()
    weather = models.CharField(max_length=50, default="Data not available")

    def __str__(self):
        return self.name

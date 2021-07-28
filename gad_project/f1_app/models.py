from django.db import models
from datetime import datetime


# class Circuit(models.Model):
#     name = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     capacity = models.DecimalField(max_digits=6, decimal_places=3)
#     gps_held = models.PositiveIntegerField()
#     length = models.DecimalField(max_digits=4, decimal_places=3)
#     lap_record = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
#
# class Race(models.Model):
#     name = models.CharField(max_length=50)
#     circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
#     first_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='first_place')
#     second_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='second_place')
#     third_place = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='third_place')
#     date = models.DateTimeField()
#     sold_out = models.BooleanField()
#
#     def __str__(self):
#         return self.name


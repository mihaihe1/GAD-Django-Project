from django.shortcuts import render
from .models import Race
# Create your views here.


def show_all_races(request):
    races = Race.objects.all()
    return render(request, "races.html", {"races": races})
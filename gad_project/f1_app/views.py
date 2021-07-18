from django.shortcuts import render
from .models import Team, Pilot

# Create your views here.


def home_view(request):
    return render(request, "home.html", {})


def team_list(request):
    teams = Team.objects.all()
    return render(request, "team_list.html", {"teams": teams})


def pilot_list(request):
    pilots = Pilot.objects.all()
    return render(request, "pilot_list.html", {"pilots": pilots})
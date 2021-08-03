from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Race
from .forms import AddRaceForm
from webscraping import weather_webscraping
from datetime import timezone, datetime


def show_all_races(request):
    races = Race.objects.all()
    return render(request, "races.html", {"races": races})


def add_race(request):
    if request.method == 'GET':
        form = AddRaceForm()

        return render(request, 'add_race.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = AddRaceForm(request.POST, request.FILES)

        if form.is_valid():
            task = form.save()
            delta = task.date - datetime.now()
            if delta.days < 10:
                task.weather = weather_webscraping(task.circuit.location, delta.days)
            task.save()
            messages.success(request, f'Race was successfully added!')

            return redirect(reverse('races:view_all'))

        # form is not valid!
        return render(request, 'add_race.html', {
            'form': form
        })

    raise Http404('Method not allowed!')

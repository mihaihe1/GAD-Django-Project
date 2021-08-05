from django.shortcuts import render, redirect, reverse, Http404, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Race
from .forms import AddRaceForm, FilterRaces
from webscraping import weather_webscraping
from datetime import timezone, datetime
from drivers.models import Driver


def show_all_races(request):
    # races = Race.objects.all()
    form = FilterRaces(request.GET)
    if form.is_valid():
        races = form.get_races()
        paginator = Paginator(races, 3)

        page = request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        return render(request, "races.html", {'page_obj': page_obj, 'form': form})


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

            first_place = Driver.objects.get(id=task.first_place.id)
            first_place.points += 3
            if first_place.highest_race_finish > 1:
                first_place.highest_race_finish = 1
            first_place.save()

            second_place = Driver.objects.get(id=task.second_place.id)
            second_place.points += 2
            if second_place.highest_race_finish > 2:
                second_place.highest_race_finish = 2
            second_place.save()

            third_place = Driver.objects.get(id=task.third_place.id)
            third_place.points += 1
            if third_place.highest_race_finish > 3:
                third_place.highest_race_finish = 3
            third_place.save()

            messages.success(request, f'Race was successfully added!')

            return redirect(reverse('races:view_all'))

        # form is not valid!
        return render(request, 'add_race.html', {
            'form': form
        })

    raise Http404('Method not allowed!')

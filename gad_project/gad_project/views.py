from django.shortcuts import render
from webscraping import standings_webscraping


def show_homepage(request):
    return render(request, 'homepage.html')


def real_standings(request):
    standings = standings_webscraping()
    # print(standings)
    return render(request, 'real_standings.html', {'standings': standings})

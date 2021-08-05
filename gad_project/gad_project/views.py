from django.shortcuts import render
from webscraping import standings_webscraping, news_webscraping
from races.models import Race
from drivers.models import Driver


def show_homepage(request):
    return render(request, 'homepage.html')


def real_standings(request):
    standings = standings_webscraping()
    # print(standings)
    return render(request, 'real_standings.html', {'standings': standings})


def custom_standings(request):
    drivers = Driver.objects.all().order_by('-points')
    standings = []
    poz = 1
    for driver in drivers:
        standings.append((poz, driver.first_name, driver.last_name, driver.country, driver.team.name, driver.points))
        poz += 1
        # print(driver.team.name)

    return render(request, 'custom_standings.html', {'standings': standings})


def news(request):
    news_list = news_webscraping()
    print(news_list)
    return render(request, 'news.html', {"news": news_list})

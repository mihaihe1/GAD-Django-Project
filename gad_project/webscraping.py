import os
import csv
import json
import requests
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
import math


def standings_webscraping():
    url = 'https://www.formula1.com/en/results.html/2021/drivers.html'
    columns = ['Position', 'Driver', 'Nationality', 'Car', 'Points']

    standings = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='html.parser')

    table = soup.find('table', {"class": "resultsarchive-table"})
    table_rows = table.find_all('tr')
    table_rows.pop(0)

    bad_classes = ['limiter', 'hide-for-tablet', 'uppercase hide-for-desktop']

    for table_row in table_rows:
        columns_list = []
        for td in table_row.find_all('td'):
            if td.find('span', class_='hide-for-mobile') is not None:
                driver = td.find('span', class_='hide-for-mobile').text
                columns_list.append(driver)

            if td.find('a', class_='grey semi-bold uppercase ArchiveLink') is not None:
                car = td.find('a', class_='grey semi-bold uppercase ArchiveLink').text
                columns_list.append(car)

            if len(td.get('class', [])) and td.get('class', [])[0] not in bad_classes:
                columns_list.append(td.text)

        dict = {
            col: data
            for col, data in zip(columns, columns_list)
        }
        standings.append(dict)

    return standings


def news_webscraping():
    url = 'https://www.formula1.com/en/latest/all.html'

    news = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='html.parser')

    grid_div = soup.find_all('div', {'class': 'f1-latest-listing--grid-item'})

    for item in grid_div:
        div = item.find('div', {'class': 'f1-cc--caption'})
        category = div.find('p', {'class': 'misc--tag'}).text.strip()

        if category == 'News':
            news_text = div.find('p', {'class': 'no-margin'}).text
            news.append(news_text)

    return news


def weather_webscraping(city, day):
    if day > 9:
        return 'No data available'

    url = f'https://www.weatherbug.com/weather-forecast/10-day-weather/{city}'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='html.parser')

    li_list = soup.find_all('li', {'class': 'day-card-list__item'})
    race_day = li_list[day]

    div = race_day.find('div', {'class': 'day-card__desktop'})
    day_temp_div = div.find('div', {'class': 'day-card__body'})

    temperature = day_temp_div.find('div', {'class': 'temp'}).text.strip()
    description = day_temp_div.find('div', {'class': 'description'}).text.strip()

    temperature_to_int = int(temperature[:-1])  # elimin ultimul caracter deoarece temperatura era de forma 92°
    temperature_to_celsius = math.floor((temperature_to_int - 32) * 5/9)  # fahrenheit -> celsius

    return f'{temperature_to_celsius}° - {description}'


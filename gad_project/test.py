from webscraping import standings_webscraping, news_webscraping, weather_webscraping

st = standings_webscraping()
ne = news_webscraping()
we = weather_webscraping('Monza, Italy', 3)
print(ne)


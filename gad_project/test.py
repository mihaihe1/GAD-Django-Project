from webscraping import standings_webscraping, news_webscraping, weather_webscraping

st = standings_webscraping()
ne = news_webscraping()
we = weather_webscraping('London', 3)
print(st)


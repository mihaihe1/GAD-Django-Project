from django.urls import path
from .views import show_all_races

app_name = 'races'

# this is in `/races/`
urlpatterns = [
    path('', show_all_races, name='view_all')
]

from django.urls import path
from .views import show_all_teams, add_team, view_team, update_team

app_name = 'teams'

# this is in `/teams/`
urlpatterns = [
    path('', show_all_teams, name='view_all'),
    path('add/', add_team, name='add'),
    path('<int:team_id>', view_team, name="view"),
    path('<int:team_id>/update/', update_team, name='update')
]

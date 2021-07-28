from django.urls import path
from .views import show_all_circuits

app_name = 'circuits'

# this is in `/circuits/`
urlpatterns = [
    path('', show_all_circuits, name='view_all'),
]

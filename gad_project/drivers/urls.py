from django.urls import path
from .views import show_all_drivers, add_driver, view_driver

app_name = 'drivers'

# this is in `/drivers/`
urlpatterns = [
    path('', show_all_drivers, name='view_all'),
    path('add/', add_driver, name='add'),
    path('<int:driver_id>', view_driver, name="view")
]

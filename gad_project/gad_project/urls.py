"""gad_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from f1_app.views import home_view, team_list, pilot_list, team_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('teams/', team_list),
    path('pilots/', pilot_list),
    path('admin/', admin.site.urls),
    path('team_create', team_create_view)
]

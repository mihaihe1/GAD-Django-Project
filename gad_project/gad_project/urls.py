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
from django.urls import path, include
from .views import show_homepage, real_standings, custom_standings, news

urlpatterns = [
    path('', show_homepage, name="home"),
    path('real_standings/', real_standings, name="real_standings"),
    path('custom_standings/', custom_standings, name="custom_standings"),
    path('news/', news, name="news"),
    path('admin/', admin.site.urls),
    path('drivers/', include('drivers.urls')),
    path('circuits/', include('circuits.urls')),
    path('races/', include('races.urls')),
    path('teams/', include('teams.urls'))
]

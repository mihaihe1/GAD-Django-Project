from django.contrib import admin
from .models import Team, Pilot, Circuit, Race

admin.site.register(Team)
admin.site.register(Pilot)
admin.site.register(Circuit)
admin.site.register(Race)

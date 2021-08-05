from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from .models import Circuit
# Register your models here.


class CircuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'gps_held', 'length_km', 'lap_record')
    list_filter = ("location", )
    search_fields = ('name__startswith', )

    def length_km(self, obj):
        return format_html("<b><i>{}</i></b>", f'{obj.length} km')
    length_km.short_description = 'LENGTH'


admin.site.register(Circuit, CircuitAdmin)

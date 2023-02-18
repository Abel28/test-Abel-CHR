from django.contrib import admin
from .models import Station
from django.contrib.admin import ModelAdmin

# Register your models here.

class StationAdmin(ModelAdmin):



    list_display = ('name', 'empty_slots', 'free_bikes', "timestamp")

    fieldsets = (
        ('Información de Estación', {'fields': (
            'name',
            'empty_slots', 
            'free_bikes', 
            'latitude', 
            'longitude',
            'timestamp',
        )}),
        ('Información Extra', {'fields':(
            'uid',
            'address',
            'ebikes',
            'has_ebikes',
            'normal_bikes',
            'payment',
            'post_code',
            'renting',
            'returning',
            'slots'
        )}),
    )


admin.site.register(Station, StationAdmin)
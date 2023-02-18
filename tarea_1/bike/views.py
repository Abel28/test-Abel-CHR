from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Station

import requests

# Create your views here.


def api_bikes(request):

    response = requests.get("http://api.citybik.es/v2/networks/bikesantiago")
    data_bikes = response.json()

    #Aqui leo la información de la API desde el archivo creado
    
    # with open("/Users/abelaguilera/Desktop/postulacion_CHR/test-Abel-CHR/tarea_1/bikes_data.json") as file:
    #     data_bikes = json.load(file)

    for station in data_bikes['network']['stations']:

        print(station)

        if 'post_code' in station['extra'].keys():
            Station.objects.get_or_create(
                id = station["id"],
                empty_slots = station['empty_slots'],
                free_bikes = station['free_bikes'],
                latitude = station['latitude'],
                longitude = station['longitude'], 
                name = station['name'],
                timestamp = station['timestamp'],
                address = station['extra']['address'],
                altitude = station['extra']['altitude'],
                ebikes = station['extra']['ebikes'],
                has_ebikes = station['extra']['has_ebikes'],
                last_updated = station['extra']['last_updated'],
                normal_bikes = station['extra']['normal_bikes'],
                payment = station['extra']['payment'],
                post_code = station['extra']['post_code'],
                renting = station['extra']['renting'],
                returning = station['extra']['returning'],
                slots = station['extra']['slots'],
                uid = station['extra']['uid']
            )
        else:
            Station.objects.get_or_create(
                id = station["id"],
                empty_slots = station['empty_slots'],
                free_bikes = station['free_bikes'],
                latitude = station['latitude'],
                longitude = station['longitude'], 
                name = station['name'],
                timestamp = station['timestamp'],
                address = station['extra']['address'],
                altitude = station['extra']['altitude'],
                ebikes = station['extra']['ebikes'],
                has_ebikes = station['extra']['has_ebikes'],
                last_updated = station['extra']['last_updated'],
                normal_bikes = station['extra']['normal_bikes'],
                payment = station['extra']['payment'],
                renting = station['extra']['renting'],
                returning = station['extra']['returning'],
                slots = station['extra']['slots'],
                uid = station['extra']['uid']
            )
    



    return HttpResponseRedirect(reverse_lazy("bike:list"))


class StationsListView(ListView):
    model = Station
    paginate_by = 20
    

    def get_context_data(self, **kwargs):

        context = super(StationsListView, self).get_context_data(**kwargs)

        filter = self.request.GET.get("search_filter")

        if filter:
            context['object_list'] = self.model.objects.filter(
                name__contains=filter
            )
            
        else:
            context['object_list'] = self.model.objects.all()
        
        return context

    

class StationsDetailView(DetailView):
    model = Station
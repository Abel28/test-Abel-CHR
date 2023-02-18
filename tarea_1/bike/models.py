from django.db import models
import uuid
from multiselectfield import MultiSelectField
from django_admin_geomap import GeoItem

# Create your models here.


class Station(models.Model, GeoItem):

    '''
    Modelo Stations en donde se almacena la información de la API
    '''

    PAYMENT_CHOICES = [
        ('key', 'Tarjeta'),
        ('transitcard', 'Tarjeta de Transito'),
        ('creditcard', 'Tarjeta de Crédito'),
        ('phone', 'Teléfono Movil')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    empty_slots = models.IntegerField("Slots")
    #extra
    free_bikes = models.IntegerField("Free Bikes", null=True, blank=True)
    latitude = models.FloatField("Latitude", null=True, blank=True)
    longitude = models.FloatField("Longitude", null=True, blank=True)
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    address = models.CharField("address", max_length=255, null=True, blank=True)
    altitude = models.FloatField(null=True, blank=True)
    ebikes = models.IntegerField(null=True, blank=True)
    has_ebikes = models.BooleanField(null=True, blank=True)
    last_updated = models.IntegerField(null=True, blank=True)
    normal_bikes = models.IntegerField(null=True, blank=True)
    payment =  MultiSelectField(choices=PAYMENT_CHOICES, null=True, blank=True)
    post_code = models.CharField(null=True, max_length=100, default=None, blank=True)
    renting = models.IntegerField(null=True, blank=True)
    returning = models.IntegerField(null=True, blank=True)
    slots = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name

    def get_url_map(self):
        from django.utils.html import format_html
        return format_html(f"http://maps.google.com/maps?z=12&t=m&q=loc:{self.latitude}+{self.longitude}")
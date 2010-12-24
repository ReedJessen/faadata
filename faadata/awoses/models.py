from django.contrib.gis.db import models
from faadata.airports.models import Airport

class AWOS(models.Model):
    identifier = models.CharField(max_length=5)
    sensor_type = models.CharField(max_length=10)
    commissioned = models.BooleanField()
    point = models.PointField(srid=4326, null=True, blank=True)
    frequency = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    second_frequency = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    telephone = models.CharField(max_length=14)
    airport = models.ForeignKey(Airport, null=True, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    effective_date = models.DateField()

    def __unicode__(self):
        return self.identifier

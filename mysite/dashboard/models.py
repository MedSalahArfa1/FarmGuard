from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.gis.db import models

class MarkerPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.PointField()

    def __str__(self):
        return self.name

class PolygonPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    geometry = models.PolygonField()

    def __str__(self):
        return self.name
    

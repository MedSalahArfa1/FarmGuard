from django.contrib.gis import admin
from django.contrib.gis import admin as gis_admin
from dashboard.models import MarkerPoint,PolygonPoint
from leaflet.admin import LeafletGeoAdmin

class MarkerAdmin(LeafletGeoAdmin):
	list_display = ("name", "location")

admin.site.register(MarkerPoint,gis_admin.OSMGeoAdmin)

class PolygonAdmin(LeafletGeoAdmin):
	list_display = ("name", "geometry")

admin.site.register(PolygonPoint,gis_admin.OSMGeoAdmin)
from dashboard.models import MarkerPoint,PolygonPoint
from django.contrib.gis.geos import Point,GEOSGeometry
from django.shortcuts import render,redirect
from django.contrib.gis.db.models.functions import Area
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MarkerSerializer,PolygonSerializer,UserSerializer


def main_view(request):
    if request.method == 'POST':
        return redirect('main_page')
    return render(request, 'index.html',{'user': request.user})

@login_required
def add_marker(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = float(request.POST.get('lat'))
        longitude = float(request.POST.get('lng'))
        point = Point(longitude, latitude)
        marker = MarkerPoint(user=request.user, name=name, location=point)
        marker.save()
        return redirect('marker_page')
    else:
        polygons = PolygonPoint.objects.filter(user=request.user)
        markers = MarkerPoint.objects.filter(user=request.user)
    return render(request, 'marker.html', {'markers': markers,'polygons':polygons})

@login_required
def add_polygon(request):
    if request.method == 'POST':
        namep = request.POST.get('nameP')
        geometry_str = request.POST.get('geometry')
        geometry = GEOSGeometry(geometry_str)
        existing_polygons = PolygonPoint.objects.all()
        polygons = PolygonPoint.objects.filter(user=request.user)
        for existing_polygon in existing_polygons:
            if existing_polygon.geometry.intersects(geometry):
                error_msg = "Your farm is superposed with another farm !"
                return render(request, 'polygon.html', {'polygons':polygons ,'error_msg': error_msg})
        polygon = PolygonPoint(user=request.user,name=namep, geometry=geometry)
        polygon.save()
        return redirect('marker_page')
    else:
        polygons = PolygonPoint.objects.filter(user=request.user)
        for polygon in polygons:
            surface_area = polygon.geometry.area
            polygon.surface_area = surface_area
    return render(request, 'polygon.html',{'polygons':polygons})

def dash_view(request):
    if request.method == 'POST':
        return redirect('dashboard_page')
    else:
        polygons = PolygonPoint.objects.filter(user=request.user)
        markers = MarkerPoint.objects.filter(user=request.user)
    return render(request, 'dashboard.html',{'user': request.user, 'markers': markers, 'polygons':polygons})

##########

@api_view(['GET'])
def fetch_markers(request):
    markers = MarkerPoint.objects.filter(user=request.user)
    serializer = MarkerSerializer(markers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_polygons(request):
    polygons = PolygonPoint.objects.filter(user=request.user)
    serializer = PolygonSerializer(polygons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fetch_user_data(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


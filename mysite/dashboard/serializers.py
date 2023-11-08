from rest_framework import serializers
from .models import MarkerPoint,PolygonPoint
from django.contrib.auth.models import User

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkerPoint
        fields = '__all__'

class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolygonPoint
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','date_joined']

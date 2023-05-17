from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.Serializer):
    points = serializers.CharField()
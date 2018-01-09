from rest_framework import serializers

from .models import Defib

class DefibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defib
        fields = ('id', 'lat', 'lon', 'notes', 'address', 'image',)
        read_only_fields = ('id', 'lat', 'lon', 'notes', 'address', 'image',)

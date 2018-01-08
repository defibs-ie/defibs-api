from rest_framework import serializers

from .models import Defib

class DefibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defib
        fields = ('lat', 'lon', 'notes',)
        read_only_fields = ('lat', 'lon', 'notes',)

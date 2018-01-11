from rest_framework import serializers

from .models import Defib

class DefibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defib
        fields = ('id', 'lat', 'lon', 'notes', 'address', 'image',)
        read_only_fields = ('id', 'lat', 'lon', 'notes', 'address', 'image',)


class SubmissionSerializer(serializers.Serializer):
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    lon = serializers.DecimalField(max_digits=9, decimal_places=6)
    notes = serializers.CharField(allow_blank=True, required=False)

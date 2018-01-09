from rest_framework import serializers

from .models import Contributor

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ('name', 'defib_count',)
        read_only_fields = ('name', 'defib_count',)

    defib_count = serializers.IntegerField(source='get_defib_count')

from django.db.models import Count
from rest_framework import mixins, viewsets

from .models import Contributor
from .serializers import ContributorSerializer

class ContributorViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Contributor.objects.annotate(defib_count=Count('defib')).order_by('-defib_count')
    serializer_class = ContributorSerializer

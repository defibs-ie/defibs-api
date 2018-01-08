from rest_framework import mixins, viewsets

from .models import Defib
from .serializers import DefibSerializer

class DefibViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Defib.objects.all()
    serializer_class = DefibSerializer

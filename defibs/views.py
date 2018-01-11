from django.conf import settings
from django.core.mail import send_mail
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Defib
from .serializers import DefibSerializer, SubmissionSerializer

class DefibViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Defib.objects.all()
    serializer_class = DefibSerializer

    @list_route(methods=['post'])
    def submit(self, request):
        sender = settings.SUBMISSION_EMAIL_FROM
        recipient = settings.SUBMISSION_EMAIL_TO
        subject = 'New defibs.ie submission'
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = SubmissionSerializer(request.data).data
            message = self.build_message(request.data)
            send_mail(
                subject,
                message,
                sender,
                [recipient],
            )
            return Response(status=status.HTTP_201_CREATED)

    
    def build_message(self, data):
        return (
            f"Submission from: {data.get('email', '<anonymous@example.com>')}\n"
            f"Latitude:\n{data['lat']}\n"
            f"Longitude:\n{data['lon']}\n\n"
            f"Notes:\n{data.get('notes', '')}"
        )

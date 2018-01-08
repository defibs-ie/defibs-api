import uuid
from django.db import models

class Defib(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    address = models.TextField(null=True, blank=True)

    notes = models.TextField(null=True, blank=True)

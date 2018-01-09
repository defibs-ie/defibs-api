import os
import uuid
from django.db import models
from django.utils.deconstruct import deconstructible

# https://coderwall.com/p/hfgoiw/give-imagefield-uploads-a-unique-name-to-avoid-file-overwrites

@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, '%s%s')

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

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

    image = models.ImageField(null=True, blank=True, upload_to=RandomFileName('uploads/'))

    def __str__(self):
        return self.address

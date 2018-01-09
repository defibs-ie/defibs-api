import uuid
from django.db import models

class Contributor(models.Model):

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    name = models.CharField(max_length=200)

    def get_defib_count(self):
        return self.defib_set.count()

    def __str__(self):
        return self.name

from django.db import models

class Defib(models.Model):

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    notes = models.TextField()

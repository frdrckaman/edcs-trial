from django.db import models
from .RetroYears import RetroYears
from django.db.models import PROTECT


class RetroYearMixn(models.Model):
    year = models.ForeignKey(RetroYears, on_delete=PROTECT, null=True)

    class Meta:
        abstract = True

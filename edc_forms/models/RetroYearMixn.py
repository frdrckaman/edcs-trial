from django.db import models
from django.db.models import PROTECT

from .RetroYears import RetroYears


class RetroYearMixin(models.Model):
    year = models.ForeignKey(RetroYears, on_delete=PROTECT, null=True)

    class Meta:
        abstract = True

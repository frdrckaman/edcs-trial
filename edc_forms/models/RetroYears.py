from django.db import models

from edc_models.base_uuid_model import BaseUuidModel
from edc_models.historical_records import HistoricalRecords


class RetroYears(BaseUuidModel):
    year = models.IntegerField(verbose_name="Retro-Year", default=0)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ("year",)
        verbose_name = "Retrospective year"
        verbose_name_plural = "Retrospective years"

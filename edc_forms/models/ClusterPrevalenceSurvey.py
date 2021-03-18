from django.db import models

from edc_models.base_uuid_model import BaseUuidModel
from edc_models.historical_records import HistoricalRecords


class ClusterPrevalenceSurvey(BaseUuidModel):
    cluster_name = models.CharField(verbose_name="Cluster Name", max_length=60)
    latitude = models.DecimalField(
        verbose_name="Latitude", max_digits=8, decimal_places=8
    )
    longitude = models.DecimalField(
        verbose_name="Longitude", max_digits=8, decimal_places=8
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Cluster Prevalence Survey"
        verbose_name_plural = "Cluster Prevalence Survey"

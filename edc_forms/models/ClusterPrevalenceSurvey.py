from django.db import models
from django.contrib.sites.models import Site
from edc_models.base_uuid_model import BaseUuidModel
# from ..studyYearMixin import StudyYearMixin
from django.urls import reverse


class ClusterPrevalenceSurvey(BaseUuidModel):
    cluster_name = models.CharField(verbose_name='Cluster Name', max_length=60)
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=8, decimal_places=8)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=8, decimal_places=8)

    class Meta:
        verbose_name = 'Cluster Prevalence Survey'
        verbose_name_plural = 'Cluster Prevalence Survey'

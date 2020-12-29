from django.db import models
from django.contrib.sites.models import Site
from edc_models.base_uuid_model import BaseUuidModel
# from ..studyYearMixin import StudyYearMixin
from django.urls import reverse


class RetroYears(BaseUuidModel):
    year = models.IntegerField(verbose_name='Retro-Year', default=0)

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Retrospective year'
        verbose_name_plural = 'Retrospective years'

from django.db import models
from django.db.models import PROTECT
from edc_forms.models import RetroYears


class StudyYearMixin:
    year = models.IntegerField(verbose_name='Year', default=0)
    # year_id = models.OneToOneField(RetroYears, on_delete=PROTECT)

    class Meta:
        abstract = True

from django.db import models
from django.contrib.sites.models import Site
from django.db.models import PROTECT

from edc_models.base_uuid_model import BaseUuidModel
from edc_models.base_model import BaseModel
from .RetroYears import RetroYears
from .RetroYearMixn import RetroYearMixn


class SmearPositiveTB(BaseUuidModel, RetroYearMixn, BaseModel):
    age_15_24 = models.IntegerField(verbose_name='15-24')
    age_25_34 = models.IntegerField(verbose_name='25-34')
    age_35_44 = models.IntegerField(verbose_name='35-44')
    age_45_54 = models.IntegerField(verbose_name='45-54')
    age_55_64 = models.IntegerField(verbose_name='55-64')
    age_65_above = models.IntegerField(verbose_name='65 and Above')
    gender_male = models.IntegerField(verbose_name='Male', default=0)
    gender_female = models.IntegerField(verbose_name='Female', default=0)
    soc_econ_pos_low = models.IntegerField(verbose_name='Low', default=0)
    soc_econ_pos_middle = models.IntegerField(verbose_name='Middle', default=0)
    soc_econ_pos_high = models.IntegerField(verbose_name='High', default=0, )

    def __str__(self):
        return str(self.year)

    class Meta:
        # ordering = ('-created',)
        verbose_name = 'Smear Positive Pulmonary TB'
        verbose_name_plural = 'Smear Positive Pulmonary TB'

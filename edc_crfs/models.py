from django.db import models

from edc_models.base_uuid_model import BaseUuidModel


class Crf(BaseUuidModel):
    name = models.CharField(verbose_name="Study CRF nme", max_length=80)
    required = models.BooleanField(verbose_name="Require CRF", default=True)

    def __str__(self):
        return str(self.name)

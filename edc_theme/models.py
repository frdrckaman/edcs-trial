from django.db import models
from edc_models.base_uuid_model import BaseUuidModel
from edc_models.user_model_mixin import UserModelMixin
from edc_models.base_model import BaseModel
from django.conf import settings

theme = [
    ('dark', 'Dark Theme'),
    ('light', 'Light Theme')
]


class EdcsTheme(BaseUuidModel, UserModelMixin, BaseModel):
    theme = models.CharField(verbose_name='EDC Theme', choices=theme, max_length=8, default=settings.EDC_THEME)

    def __str__(self):
        return str(self.theme)

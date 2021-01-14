from django.db import models
from edc_models.base_uuid_model import BaseUuidModel

theme = [
    ('dark', 'Dark Theme'),
    ('light', 'Light Theme')
]


class EdcsTheme(BaseUuidModel):
    theme = models.CharField(verbose_name='Dark Mode', choices=theme, max_length=8)

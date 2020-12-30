from django import forms

from edc import settings
from .models import SmearPositiveTB
from .retro_year_mixin import RetroYearFormMixin


class SmearPositiveTBForm(RetroYearFormMixin):
    pass

    class Meta:
        model = SmearPositiveTB
        fields = "__all__"

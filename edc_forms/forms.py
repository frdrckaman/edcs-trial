from django import forms

from edc import settings
from .models import SmearPositiveTB, RetroYears
from .models import RetroYearMixn
from .retro_year_mixin import RetroYearFormMixin


class SmearPositiveTBForm(RetroYearFormMixin):
    pass

    class Meta:
        model = SmearPositiveTB
        fields = "__all__"


class RetroYearMixinForm(forms.ModelForm):
    class Meta:
        model = RetroYears
        fields = "__all__"

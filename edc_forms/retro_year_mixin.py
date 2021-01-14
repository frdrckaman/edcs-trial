from django import forms
from .models import RetroYears
from edc_forms.models import SmearPositiveTB


class RetroYearFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('initial'):
            self.fields['year'].empty_label = None


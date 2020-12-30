from django import forms
from .models import RetroYears


class RetroYearFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subject_id = RetroYears.objects.filter(id=kwargs.get('initial')['subject_id'])
        self.fields['year'].queryset = subject_id
        self.fields['year'].empty_label = None

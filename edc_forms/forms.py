from django import forms
from .models import SmearPositiveTB


class SmearPositiveTBForm(forms.ModelForm):
    class Meta:
        model = SmearPositiveTB
        fields = "__all__"

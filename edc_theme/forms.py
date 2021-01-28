from pprint import pprint

from django import forms
from edc_theme.models import EdcsTheme


class EdcsThemeForm(forms.ModelForm):

    def save(self, commit=True):
        if EdcsTheme.objects.filter(user_id=self.data.get('user')):
            pprint('frdrck')
            EdcsTheme.objects.filter(user_id=self.data.get('user')).update(theme=self.cleaned_data.get('theme'))
        else:
            EdcsTheme.objects.create(theme=self.cleaned_data.get('theme'))

    class Meta:
        model = EdcsTheme
        fields = '__all__'

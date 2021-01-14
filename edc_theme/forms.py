from django import forms
from edc_theme.models import EdcsTheme


class EdcsThemeForm(forms.ModelForm):

    def save(self, commit=True):
        EdcsTheme.objects.filter(id=self.data.get('uuid')).update(theme=self.cleaned_data.get('theme'))

    class Meta:
        model = EdcsTheme
        fields = '__all__'

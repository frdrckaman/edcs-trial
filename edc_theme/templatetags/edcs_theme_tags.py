from django import template
from edc_theme.models import EdcsTheme

register = template.Library()


@register.simple_tag
def theme_tag():
    return EdcsTheme.objects.values('theme')[0]['theme']


@register.simple_tag
def theme_next():
    if EdcsTheme.objects.values('theme')[0]['theme'] == 'light':
        theme = 'dark'
    else:
        theme = 'light'
    return theme


@register.simple_tag
def theme_name():
    if EdcsTheme.objects.values('theme')[0]['theme'] == 'dark':
        return 'Light Mode'
    else:
        return 'Dark Mode'


@register.simple_tag
def theme_id():
    return EdcsTheme.objects.values('id')[0]['id']

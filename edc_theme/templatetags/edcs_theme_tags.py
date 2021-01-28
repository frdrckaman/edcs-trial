from django import template
from edc_theme.models import EdcsTheme
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

register = template.Library()


@register.simple_tag
def theme_tag():
    return EdcsTheme.objects.filter(user_id=get_current_user().id).first()


@register.simple_tag
def theme_next():
    if EdcsTheme.objects.filter(user_id=get_current_user().id).first().theme == 'light':
        theme = 'dark'
    else:
        theme = 'light'
    return theme


@register.simple_tag
def theme_name():
    if EdcsTheme.objects.filter(user_id=get_current_user().id).first().theme == 'dark':
        return 'Light Mode'
    else:
        return 'Dark Mode'


@register.simple_tag
def theme_id():
    return EdcsTheme.objects.filter(user_id=get_current_user().id).first().id


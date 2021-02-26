from django import template
from django.conf import settings
from edc_theme.models import EdcsTheme
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

register = template.Library()


@register.simple_tag
def theme_tag():
    if get_current_authenticated_user():
        return EdcsTheme.objects.filter(user_id=get_current_user().id).first()
    else:
        return settings.EDC_THEME


@register.simple_tag
def theme_next():
    if get_current_authenticated_user():
        if EdcsTheme.objects.filter(user_id=get_current_user().id).first().theme == 'light':
            theme = 'dark'
        else:
            theme = 'light'
    else:
        theme = settings.EDC_THEME
    return theme


@register.simple_tag
def theme_name():
    if get_current_authenticated_user():
        if EdcsTheme.objects.filter(user_id=get_current_user().id).first().theme == 'dark':
            theme = 'Light Mode'
        else:
            theme = 'Dark Mode'
    else:
        theme = settings.EDC_THEME_MODE
    return theme


@register.simple_tag
def theme_id():
    if get_current_authenticated_user():
        return EdcsTheme.objects.filter(user_id=get_current_user().id).first().id


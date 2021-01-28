from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from edc_theme.models import EdcsTheme


@admin.register(EdcsTheme)
class EdcsThemeAdmin(admin.ModelAdmin):
    list_display = ('theme', 'created')
    fields = ('theme',)

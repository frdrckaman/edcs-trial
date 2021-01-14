from django.contrib import admin
from edc_theme.models import EdcsTheme


@admin.register(EdcsTheme)
class EdcsThemeAdmin(admin.ModelAdmin):
    list_display = ('theme', 'created')
    fields = ('theme', )

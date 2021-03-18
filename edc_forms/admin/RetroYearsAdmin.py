from django.contrib import admin

from edc_models.admin import SimpleHistoryAdmin

from ..admin_site import edc_forms_admin
from ..models import RetroYears


@admin.register(RetroYears, site=edc_forms_admin)
class RetroYearsAdmin(SimpleHistoryAdmin):
    list_display = ("year",)
    fields = ("year",)

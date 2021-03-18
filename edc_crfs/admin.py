from django.contrib import admin

from edc_models.admin import SimpleHistoryAdmin

from .admin_site import edc_crfs_admin
from .models import Crf


@admin.register(Crf, site=edc_crfs_admin)
class CrfAdmin(SimpleHistoryAdmin):
    list_display = (
        "name",
        "created",
    )
    fields = ("name", "required")
    list_filter = ("required",)

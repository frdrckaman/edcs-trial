from django.contrib import admin

from edc_models.admin import SimpleHistoryAdmin

from ..admin_site import edc_forms_admin
from ..models import ClusterPrevalenceSurvey


@admin.register(ClusterPrevalenceSurvey, site=edc_forms_admin)
class ClusterPrevalenceSurveyAdmin(SimpleHistoryAdmin):
    # list_display = ('created', 'updated')
    # ordering = ('created',)
    fields = ("cluster_name", "latitude", "longitude")

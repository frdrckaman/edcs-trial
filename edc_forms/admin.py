from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .admin_site import edc_forms_admin
from .forms import SmearPositiveTBForm
from .models import (
    BacteriologicalConfirmedPulmonaryTB,
    ClusterPrevalenceSurvey,
    RetroYears,
    SmearPositiveTB,
)

# class SmearAdmin(AdminSite):
#     site_header = 'Smear Positive TB'
#
#
# admin_site = SmearAdmin(name='smearAdmin')
# admin_site.register(SmearPositiveTB)


@admin.register(SmearPositiveTB, site=edc_forms_admin)
class SmearPositiveTBAdmin(SimpleHistoryAdmin):
    form = SmearPositiveTBForm
    list_display = ("created",)
    # ordering = ('created',)
    fieldsets = (
        (None, {"fields": ("year",)}),
        (
            "AGE GROUP",
            {
                "fields": (
                    "age_15_24",
                    "age_25_34",
                    "age_35_44",
                    "age_45_54",
                    "age_55_64",
                    "age_65_above",
                )
            },
        ),
        ("GENDER", {"fields": ("gender_male", "gender_female")}),
        (
            "SOCIAL ECONOMIC POSITION",
            {
                "fields": (
                    "soc_econ_pos_low",
                    "soc_econ_pos_middle",
                    "soc_econ_pos_high",
                )
            },
        ),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.GET.get("subject_id"):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                pk=request.GET.get("subject_id", 0)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        if not request.GET.get("subject_id") and "subject_id" not in readonly_fields:
            return self.readonly_fields + ("year",)
        return self.readonly_fields


@admin.register(BacteriologicalConfirmedPulmonaryTB, site=edc_forms_admin)
class BacteriologicalConfirmedPulmonaryTBAdmin(admin.ModelAdmin):
    # list_display = ('created',)
    # ordering = ('created',)
    fieldsets = (
        (
            "AGE GROUP",
            {
                "fields": (
                    "age_15_24",
                    "age_25_34",
                    "age_35_44",
                    "age_45_54",
                    "age_55_64",
                    "age_65_above",
                )
            },
        ),
        ("GENDER", {"fields": ("gender_male", "gender_female")}),
        (
            "SOCIAL ECONOMIC POSITION",
            {
                "fields": (
                    "soc_econ_pos_low",
                    "soc_econ_pos_middle",
                    "soc_econ_pos_high",
                )
            },
        ),
    )


@admin.register(ClusterPrevalenceSurvey, site=edc_forms_admin)
class ClusterPrevalenceSurveyAdmin(admin.ModelAdmin):
    # list_display = ('created', 'updated')
    # ordering = ('created',)
    fields = ("cluster_name", "latitude", "longitude")


@admin.register(RetroYears, site=edc_forms_admin)
class RetroYearsAdmin(admin.ModelAdmin):
    list_display = ("year",)
    fields = ("year",)

from django.contrib import admin

from edc_models.admin import SimpleHistoryAdmin

from ..admin_site import edc_forms_admin
from ..models import BacteriologicalConfirmedPulmonaryTB


@admin.register(BacteriologicalConfirmedPulmonaryTB, site=edc_forms_admin)
class BacteriologicalConfPulTbAdmin(SimpleHistoryAdmin):
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

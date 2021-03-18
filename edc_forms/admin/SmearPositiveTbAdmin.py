from django.contrib import admin

from edc_models.admin import SimpleHistoryAdmin

from ..admin_site import edc_forms_admin
from ..forms import SmearPositiveTBForm
from ..models import SmearPositiveTB


@admin.register(SmearPositiveTB, site=edc_forms_admin)
class SmearPositiveTBAdmin(SimpleHistoryAdmin):

    form = SmearPositiveTBForm
    list_display = (
        "created",
        "age_15_24",
        "age_25_34",
        "gender_male",
        "gender_female",
    )
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

    def render_change_form(
        self,
        request,
        context,
        add=False,
        change=False,
        form_url="",
        obj=None,
    ):
        context.update(
            {
                "show_save": True,
                "show_save_and_continue": False,
                "show_save_and_add_another": False,
                "show_delete": False,
            }
        )
        return super().render_change_form(request, context, add, change, form_url, obj)

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

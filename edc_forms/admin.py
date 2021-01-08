from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.safestring import mark_safe
from .forms import SmearPositiveTBForm
from .models import SmearPositiveTB, BacteriologicalConfirmedPulmonaryTB, ClusterPrevalenceSurvey, RetroYears


# class SmearAdmin(AdminSite):
#     site_header = 'Smear Positive TB'
#
#
# admin_site = SmearAdmin(name='smearAdmin')
# admin_site.register(SmearPositiveTB)


@admin.register(SmearPositiveTB)
class SmearPositiveTBAdmin(admin.ModelAdmin):
    form = SmearPositiveTBForm
    list_display = ('created',)
    # ordering = ('created',)
    fieldsets = (
        (None, {"fields": ("year", )}),
        ('AGE GROUP',
         {
             'fields': (
                 'age_15_24',
                 'age_25_34',
                 'age_35_44',
                 'age_45_54',
                 'age_55_64',
                 'age_65_above',
             )
         },
         ),
        ('GENDER', {'fields': ('gender_male', 'gender_female')}),
        ('SOCIAL ECONOMIC POSITION', {'fields': ('soc_econ_pos_low', 'soc_econ_pos_middle', 'soc_econ_pos_high')})
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.GET.get("subject_id"):
            kwargs["queryset"] = db_field.related_model.objects.filter(
                pk=request.GET.get("subject_id", 0)
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(BacteriologicalConfirmedPulmonaryTB)
class BacteriologicalConfirmedPulmonaryTBAdmin(admin.ModelAdmin):
    # list_display = ('created',)
    # ordering = ('created',)
    fieldsets = (
        ('AGE GROUP',
         {
             'fields': (
                 'age_15_24',
                 'age_25_34',
                 'age_35_44',
                 'age_45_54',
                 'age_55_64',
                 'age_65_above',
             )
         },
         ),
        ('GENDER', {'fields': ('gender_male', 'gender_female')}),
        ('SOCIAL ECONOMIC POSITION', {'fields': ('soc_econ_pos_low', 'soc_econ_pos_middle', 'soc_econ_pos_high')})
    )


@admin.register(ClusterPrevalenceSurvey)
class ClusterPrevalenceSurveyAdmin(admin.ModelAdmin):
    # list_display = ('created', 'updated')
    # ordering = ('created',)
    fields = ('cluster_name', 'latitude', 'longitude')


@admin.register(RetroYears)
class RetroYearsAdmin(admin.ModelAdmin):
    list_display = ('year',)
    fields = ('year',)

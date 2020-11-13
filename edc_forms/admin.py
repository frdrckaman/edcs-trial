from django.contrib import admin
from .models import SmearPositiveTB, BacteriologicalConfirmedPulmonaryTB, ClusterPrevalenceSurvey


@admin.register(SmearPositiveTB)
class SmearPositiveTBAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)
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


@admin.register(BacteriologicalConfirmedPulmonaryTB)
class BacteriologicalConfirmedPulmonaryTBAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)


@admin.register(ClusterPrevalenceSurvey)
class ClusterPrevalenceSurveyAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)

from django.contrib import admin
from .models import SmearPositiveTB, BacteriologicalConfirmedPulmonaryTB, ClusterPrevalenceSurvey


@admin.register(SmearPositiveTB)
class SmearPositiveTBAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)


@admin.register(BacteriologicalConfirmedPulmonaryTB)
class BacteriologicalConfirmedPulmonaryTBAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)


@admin.register(ClusterPrevalenceSurvey)
class ClusterPrevalenceSurveyAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'site')
    ordering = ('created',)

from django.contrib import admin
from django.urls import path

from edc_dashboard.views import DashboardView, DataDashboardView, DataFormsView

app_name = "edc_dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("data-dashboard/", DataDashboardView.as_view(), name="data-dashboard"),
    path("data-record/<yr>/<uuid>/", DataFormsView.as_view(), name="data-record"),
]

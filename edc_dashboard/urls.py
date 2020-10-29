from django.urls import path
from edc_dashboard.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
]
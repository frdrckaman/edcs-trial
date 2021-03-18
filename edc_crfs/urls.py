from django.urls import path

from edc_crfs.admin_site import edc_crfs_admin
from edc_dashboard.views import DashboardView, DataDashboardView, DataFormsView

app_name = "edc_crfs"

urlpatterns = [
    path("admin/", edc_crfs_admin.urls),
]

from django.urls import path

from .admin_site import edc_forms_admin
from .views import SmearPositiveTBView

app_name = "edc_forms"

urlpatterns = [
    path("admin/", edc_forms_admin.urls),
    path("", SmearPositiveTBView.as_view(), name="smear"),
]

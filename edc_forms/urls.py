from django.urls import path
from django.views.generic import RedirectView

from .admin_site import edc_forms_admin
from .views import SmearPositiveTBView

app_name = "edc_forms"

urlpatterns = [
    path("admin/", edc_forms_admin.urls),
    # path("", RedirectView.as_view(url="/edc_forms/admin/"), name="home_url"),
    path("", SmearPositiveTBView.as_view(), name="smear"),
]

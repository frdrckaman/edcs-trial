from django.urls import path
from django.contrib import admin
from .admin_site import edcs_form_admin
from .views import SmearPositiveTBView

app_name = 'edc_forms'

urlpatterns = [
    path("admin/", edcs_form_admin.urls),
    path('', SmearPositiveTBView.as_view(), name='smear')
]
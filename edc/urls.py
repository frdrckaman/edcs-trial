from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from edc_crfs.admin_site import edc_crfs_admin
from edc_dashboard.views import AdministrationView, DashboardView
from edc_forms.admin_site import edc_forms_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/", edc_forms_admin.urls),
    path("admin/", edc_crfs_admin.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("edc_auth.urls")),
    path("dashboard/", include("edc_dashboard.urls")),
    path("edc_forms/", include("edc_forms.urls")),
    path("edc_crfs/", include("edc_crfs.urls")),
    path("navbar", include("edc_navbar.urls")),
    path("theme", include("edc_theme.urls")),
    path("administration/", AdministrationView.as_view(), name="administration_url"),
    path("home/", DashboardView.as_view(), name="home"),
]

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        path("", include("edc_auth.urls")),
        path("admin/", admin.site.urls),
    ]

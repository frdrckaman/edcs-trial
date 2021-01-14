from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from edc_forms.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('smearAdmin/', admin_site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('edc_auth.urls')),
    # path('dashboard/', include('edc_dashboard.urls', namespace='edc_dashboard')),
    path('dashboard/', include('edc_dashboard.urls')),
    path('forms', include('edc_forms.urls')),
    path('navbar', include('edc_navbar.urls')),
    path('theme', include('edc_theme.urls')),
]

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', include('edc_auth.urls')),
        path('admin/', admin.site.urls),
    ]

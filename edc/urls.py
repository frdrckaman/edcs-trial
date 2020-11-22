from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edc_auth.urls')),
    path('dashboard/', include('edc_dashboard.urls')),
    path('forms', include('edc_forms.urls')),
]

if settings.DEBUG and settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', include('edc_auth.urls')),
        path('admin/', admin.site.urls),
    ]

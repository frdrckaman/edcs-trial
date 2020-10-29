from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edc_auth.urls')),
    path('dashboard/', include('edc_dashboard.urls')),
]

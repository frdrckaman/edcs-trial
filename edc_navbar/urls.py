from django.urls import path
from django.contrib import admin


app_name = 'edc_navbar'

urlpatterns = [
    path('admin/', admin.site.urls, name='administration'),
]

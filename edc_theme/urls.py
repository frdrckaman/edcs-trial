from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import EdcsThemeView


urlpatterns = [
    path('', EdcsThemeView.as_view(), name='theme'),

]
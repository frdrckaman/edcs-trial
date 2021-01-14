from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from edc_theme.models import EdcsTheme
from .forms import EdcsThemeForm


class EdcsThemeView(View):
    def get(self, request, *args, **kwargs):
        if request.GET:
            form = EdcsThemeForm(request.GET)
            if form.is_valid():
                form.save()
            return redirect(request.GET.get('next'))

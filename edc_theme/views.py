from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from edc_theme.models import EdcsTheme
from .forms import EdcsThemeForm


class EdcsThemeView(View):
    def get(self, request, *args, **kwargs):
        if request.GET:
            # turn _mutable to true so that we can add data(user id) on GET then turn back false
            request.GET._mutable = True
            request.GET['user'] = request.user.id
            request.GET._mutable = False
            form = EdcsThemeForm(request.GET)
            print(form.errors)
            if form.is_valid():
                form.save()
            return redirect(request.GET.get('next'))

from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from edc_forms.models import SmearPositiveTB, RetroYears


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'edc_dashboard/bootstrap3/dashboard.html', {'data': SmearPositiveTB})

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DataDashboardView(View):
    def get(self, request, *args, **kwargs):
        years = RetroYears.objects.all()
        return render(request, 'edc_dashboard/bootstrap3/data-dashboard.html', {'years': years})


class DataFormsView(View):
    def get(self, request, *args, **kwargs):
        years = RetroYears.objects.all()
        data = SmearPositiveTB()
        context = {'years': years, 'data': data, 'subject_id': kwargs['uuid']}
        return render(request, 'edc_dashboard/bootstrap3/data-record.html', context)

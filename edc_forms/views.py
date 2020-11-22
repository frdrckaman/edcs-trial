from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from edc_sites.get_site_id import get_user_site


class SmearPositiveTBView(View):
    def get(self, request):
        get_user_site(request)
        return render(self.request, 'edc_forms/bootstrap3/smearpositiveTB.html', {})

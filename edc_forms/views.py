from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import View


class SmearPositiveTBView(View):
    def get(self, request):
        return render(self.request, 'edc_forms/bootstrap3/smearpositiveTB.html', {})

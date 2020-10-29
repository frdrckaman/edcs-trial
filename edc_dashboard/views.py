from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


class DashboardView(View):
    def get(self, request):
        return render(request, 'edc_dashboard/bootstrap3/dashboard.html', {})

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



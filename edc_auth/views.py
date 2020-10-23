from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    template_name = f'edc_auth/bootstrap{settings.EDC_BOOTSTRAP}/login.html'

    def get_context_data(self, **kwargs):
        self.request.session.set_test_cookie()
        if not self.request.session.set_test_cookie():
            messages.add_message(self.request, messages.ERROR, 'Please enable cookies.')
        self.request.session.delete_test_cookie()
        return super().get_context_data(**kwargs)


class LogoutView(BaseLogoutView):
    next_page = 'login'

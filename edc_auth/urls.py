from django.urls import path, include
from .views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name='edc_auth/bootstrap3/login.html'), name='logout'),
]
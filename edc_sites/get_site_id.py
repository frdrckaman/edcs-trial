from pprint import pprint

from django.apps import apps as django_apps
from edc_auth.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class InvalidSiteError(Exception):
    pass


def get_user_site(request):
    user_id = UserProfile.objects.get(user=request.user.id)
    site_id = user_id.sites.all()
    return site_id[0].id


def get_site_id(value, sites=None):
    """Expects sites list has elements of format
    (SITE_ID(int), site_name(char), site_long_name(char)).
    """
    if not sites:
        EdcSite = django_apps.get_model("edc_sites.edcsite")
        sites = [(obj.id, obj.name, obj.title) for obj in EdcSite.objects.all()]

    try:
        site_id = [site for site in sites if site[1] == value][0][0]
    except IndexError:
        try:
            site_id = [site for site in sites if site[2] == value][0][0]
        except IndexError:
            site_ids = [site[1] for site in sites]
            site_names = [site[2] for site in sites]
            raise InvalidSiteError(
                f"Invalid site. Got '{value}'. Expected one of "
                f"{site_ids} or {site_names}."
            )
    return site_id

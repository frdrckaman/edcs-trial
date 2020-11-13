from pprint import pprint

from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site
from edc_sites.models import SiteProfile


class AdminSite(DjangoAdminSite):

    site_title = "CRFs"
    site_header = "CRFs"
    index_title = "CRFs"
    site_url = "/admin/"

    def each_context(self, request):
        context = super().each_context(request)
        title = SiteProfile.objects.get(site=get_current_site(request)).title
        pprint(title)
        context.update(global_site=get_current_site(request))
        label = f"EDCS: {title.title()} - Forms"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


edcs_form_admin = AdminSite(name="edcs_form_admin")
# inte_subject_admin.disable_action("delete_selected")

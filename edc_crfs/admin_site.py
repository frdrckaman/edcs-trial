from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


class AdminSite(DjangoAdminSite):

    site_title = "CRFs"
    site_header = "CRFs"
    index_title = "CRFs"
    site_url = "/administration/"

    def each_context(self, request):
        context = super().each_context(request)
        title = ""
        context.update(global_site=get_current_site(request))
        label = f"EDCS: {title.title()} - CRFs"
        context.update(site_title=label, site_header=label, index_title=label)
        return context


edc_crfs_admin = AdminSite(name="edc_crfs_admin")

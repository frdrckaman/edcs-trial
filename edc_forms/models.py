from pprint import pprint

from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.contrib.sites.models import Site

# put validator
from django.urls import reverse

SEX = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))


class SmearPositiveTB(models.Model):
    age_15_24 = models.IntegerField(verbose_name='15-24')
    age_25_34 = models.IntegerField(verbose_name='25-34')
    age_35_44 = models.IntegerField(verbose_name='35-44')
    age_45_54 = models.IntegerField(verbose_name='45-54')
    age_55_64 = models.IntegerField(verbose_name='55-64')
    age_65_above = models.IntegerField(verbose_name='65 and Above')
    sex = models.CharField(verbose_name='GENDER', choices=SEX, max_length=12, default=None)
    soc_econ_pos_low = models.IntegerField(verbose_name='Low', default=0)
    soc_econ_pos_middle = models.IntegerField(verbose_name='Middle', default=0)
    soc_econ_pos_high = models.IntegerField(verbose_name='High', default=0, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    on_site = CurrentSiteManager()

    def get_admin_url(self):
        pprint(reverse('admin:index'))
        return reverse("admin:%s_%s_add" % (self._meta.app_label, self._meta.model_name))

    class Meta:
        ordering = ('-created',)


class BacteriologicalConfirmedPulmonaryTB(models.Model):
    age_15_24 = models.IntegerField(verbose_name='15-24')
    age_25_34 = models.IntegerField(verbose_name='25-34')
    age_35_44 = models.IntegerField(verbose_name='35-44')
    age_45_54 = models.IntegerField(verbose_name='45-54')
    age_55_64 = models.IntegerField(verbose_name='55-64')
    age_65_above = models.IntegerField(verbose_name='65 and Above')
    sex = models.CharField(verbose_name='GENDER', choices=SEX, max_length=12, default=None)
    soc_econ_pos_low = models.IntegerField(verbose_name='Low', default=0)
    soc_econ_pos_middle = models.IntegerField(verbose_name='Middle', default=0)
    soc_econ_pos_high = models.IntegerField(verbose_name='High', default=0, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    on_site = CurrentSiteManager()

    class Meta:
        ordering = ('-created',)


class ClusterPrevalenceSurvey(models.Model):
    cluster_name = models.CharField(verbose_name='Cluster Name', max_length=60)
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=8, decimal_places=8)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=8, decimal_places=8)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    on_site = CurrentSiteManager()

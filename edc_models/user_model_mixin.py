from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User
from django.db.models import PROTECT


class UserModelMixin(models.Model):
    user = CurrentUserField()

    class Meta:
        abstract = True

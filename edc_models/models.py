from django_audit_fields.models import AuditModelMixin
from django_audit_fields.models import AuditUuidModelMixin
from django.db import models


class MyModel(AuditModelMixin, models.Model):
    ...

    class Meta(AuditModelMixin.Meta):
        pass

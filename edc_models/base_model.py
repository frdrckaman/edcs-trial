from django.db import models
from simple_history import register
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

# Track History for a Third-Party Model
register(User)


class BaseModel(models.Model):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

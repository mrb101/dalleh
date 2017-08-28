from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now=True, auto_now_add=False, db_index=True)
    upadted = models.DateTimeField(auto_now=False, auto_now_add=True, db_index=True)

    class Meta:
        abstract = True

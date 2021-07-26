from django.db import models
from django.db.models.fields import related


class Weekday(models.Model):
    day = models.CharField(max_length=10)
    chore = models.ManyToManyField(
        "Chore", through="ChoreDay", related_name="chore")

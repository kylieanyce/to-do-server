from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.db.models.deletion import CASCADE


class Chore(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, null=True, max_length=250)
    user = models.ForeignKey(User, on_delete=CASCADE)
    weekday = models.ManyToManyField(
        "Weekday", through="ChoreDay", related_name="weekday")

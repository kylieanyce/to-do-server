from django.db import models


class ChoreDay(models.Model):
    chore = models.ForeignKey("Chore", on_delete=models.CASCADE)
    day = models.ForeignKey("Weekday", on_delete=models.CASCADE)

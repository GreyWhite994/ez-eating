from django.db import models
from django.conf import settings

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    guest_number = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )
    class Meta:
        unique_together = ('date', 'time',)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    review = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
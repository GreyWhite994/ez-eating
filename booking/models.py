from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    guest_number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

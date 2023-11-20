from django.db import models
from django.conf import settings

# Create your models here

class Reservation(models.Model):
    """Reservation class model for database

    Includes fields for name,date,time and guest_number.
    Also takes the current user who is logged in, in order to associate reservations with accounts.
    Includes a unique_together clause so that a double booking for same date/time will not occur.

    returns self.name
    """
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
    """Review model class for database

    Takes users name and review, date field is provided but is pulled from current datetime.
    
    returns self.name
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    review = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
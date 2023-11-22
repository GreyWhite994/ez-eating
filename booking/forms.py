from django import forms
from .models import Reservation, Review
import datetime
from django.core.exceptions import ValidationError


"""time_choices and guest_number choices to prevent user from picking a disallowed time
or going over the max amount of allowed persons per table"""
time_choices = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(11, 22)]
guest_number_choices = (
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
)


class ReservationForm(forms.ModelForm):
    """ ReservationForm class

    Takes Reservation Model.
    Includes a function to prevent users from choosing a date in the past when making a reservation.
    Includes Meta class and widgets for date, time and guest_number.
    Time and guest_number take constraints to limit their options
    """
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'guest_number']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=time_choices),
            'guest_number': forms.Select(choices=guest_number_choices)
        }
        
class ReviewForm(forms.ModelForm):
    """ReviewForm class

    Takes Review Model. 
    Allows users to input name and their review of the restuarant.
    Date of review is imported from datetime.

    """
    class Meta:
        model = Review
        fields = ['name', 'review']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'review': forms.Textarea(attrs={
                'rows': 5,
                'class': "form-control",
                'style': 'max-width: 600px;',
                'placeholder': 'Review'}),
        }

from django import forms
from .models import Reservation
import datetime
from django.core.exceptions import ValidationError

time_choices = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(11, 22)]

class ReservationForm(forms.ModelForm):
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
            'time': forms.Select(choices=time_choices)
        }
        

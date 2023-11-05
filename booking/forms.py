from django import forms
from .models import Reservation
from datetime import date
from django.core.exceptions import ValidationError


class ReservationForm(forms.ModelForm):
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'guest_number']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

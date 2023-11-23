from django.test import TestCase
from .forms import ReservationForm, ReviewForm

class TestReservationForm(TestCase):
    def test_reservation_name_is_required(self):
        form = ReservationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

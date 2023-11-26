from django.test import TestCase
from .forms import ReservationForm, ReviewForm

class TestReservationForm(TestCase):

    def test_reservation_name_is_required(self):
        """
        Checks whether name is a required field on ReservationForm
        """
        form = ReservationForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_reservation_date_is_required(self):
        """
        Checks whether date is a required field on ReservationForm
        """
        form = ReservationForm({'date': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors.keys())
        self.assertEqual(form.errors['date'][0], 'This field is required.')

    def test_reservation_time_is_required(self):
        """
        Checks whether time is a required field on ReservationForm
        """
        form = ReservationForm({'time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('time', form.errors.keys())
        self.assertEqual(form.errors['time'][0], 'This field is required.')

    def test_reservation_guest_is_required(self):
        """
        Checks whether guest_number is a required field on ReservationForm
        """
        form = ReservationForm({'guest_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('guest_number', form.errors.keys())
        self.assertEqual(form.errors['guest_number'][0], 'This field is required.')

class TestReviewForm(TestCase):

    def test_review_name_is_required(self):
        """
        Checks whether name is a required field on ReviewForm
        """
        form = ReviewForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_review_review_is_required(self):
        """
        Checks whether review is a required field on ReviewForm
        """
        form = ReviewForm({'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['review'][0], 'This field is required.')
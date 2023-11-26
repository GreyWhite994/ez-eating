from django.test import TestCase
from .models import Reservation, Review

class TestModels(TestCase):

    def test_reservation_string_method_returns_name(self):
        """
        Test to see if creating reservation object returns str(reservation)
        """
        reservation = Reservation.objects.create(name='Test Reservation Item',
        date='2022-11-22', time='11:00', guest_number=6)
        self.assertEqual(str(reservation), 'Test Reservation Item')

    def test_review_string_method_returns_name(self):
        """
        Test to see if creating review object returns str(reservation)
        """
        review = Review.objects.create(name='Test Review Item', date='2022-11-22')
        self.assertEqual(str(review), 'Test Review Item')

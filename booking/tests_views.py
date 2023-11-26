from django.test import TestCase
from .models import Reservation, Review

class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_booking_list_page(self):
        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_create_reservation_page(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_reservation.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_reservation_page(self):
        reservation = Reservation.objects.create(name='Test Reservation Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_reservation.html')
        self.assertTemplateUsed(response, 'base.html')
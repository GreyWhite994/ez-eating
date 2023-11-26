from django.test import TestCase
from .models import Reservation, Review

class TestViews(TestCase):

    def test_get_home(self):
        """
        Test to see if request for / returns 200 response
        and correct templates
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_menu(self):
        """
        Test to see if request for /menu returns 200 response
        and correct templates
        """
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_booking_list_page(self):
        """
        Test to see if request for /booking returns 200 response
        and correct templates
        """
        response = self.client.get('/booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_review_page(self):
        """
        Test to see if request for /review returns 200 response
        and correct templates
        """
        response = self.client.get('/review')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_create_reservation_page(self):
        """
        Test to see if request for /create returns 200 response
        and correct templates
        """
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_reservation.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_reservation(self):
        """
        Test to see if creating reservation object gives correct response returns 302 redirect response
        """
        response = self.client.post('/create', {'name': 'Test Added Reservation', 
        'date': '2022-11-22', 'time': '11:00', 'guest_number': 6})
        self.assertRedirects(response, '/booking')

    def test_get_edit_reservation_page(self):
        """
        Test to see if Test Reservation Item is edited and correct response given and templates used
        """
        reservation = Reservation.objects.create(name='Test Reservation Item', 
        date='2022-11-22', time='11:00', guest_number=6)
        response = self.client.get(f'/edit/{reservation.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_reservation.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_can_delete_reservation(self):
        """
        Test to see if Test Reservation Item is deleted and correct response given and redirect
        Also checks to see if Item has been correctly removed from database
        """
        reservation = Reservation.objects.create(name='Test Reservation Item', 
        date='2022-11-22', time='11:00', guest_number=6)
        response = self.client.get(f'/delete/{reservation.id}')
        self.assertRedirects(response, '/booking')
        existing_reservations = Reservation.objects.filter(id=reservation.id)
        self.assertEqual(len(existing_reservations), 0)

    def test_can_add_review(self):
        """
        Test to see if creating review object gives correct response returns 302 redirect response
        """
        response = self.client.post('/review', {'name': 'Test Added Reservation', 
        'review': 'review'})
        self.assertRedirects(response, '/')

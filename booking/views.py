from django.shortcuts import render
from .models import Reservation

# Create your views here.


def get_booking_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'booking/booking_list.html', context)

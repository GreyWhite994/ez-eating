from django.shortcuts import render, redirect
from .models import Reservation

# Create your views here.


def get_booking_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'booking/booking_list.html', context)


def create_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('reservation_name')
        date = request.POST.get('reservation_date')
        time = request.POST.get('reservation_time')
        guest_number = request.POST.get('reservation_guest_number')
        Reservation.objects.create(
            name=name, date=date, time=time, guest_number=guest_number)
        return redirect('get_booking_list')
    return render(request, 'booking/create_reservation.html')

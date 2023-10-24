from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.


def get_booking_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'booking/booking_list.html', context)


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'booking/create_reservation.html', context)

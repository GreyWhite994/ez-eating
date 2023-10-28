from django.shortcuts import render, redirect, get_object_or_404
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


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_reservation.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation, Review
from .forms import ReservationForm, ReviewForm 
import datetime


@login_required
def get_booking_list(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'booking_list.html', context)


def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('get_booking_list')
    else:
        form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'create_reservation.html', context)


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
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return redirect('get_booking_list')

def get_home(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'index.html', context)

def get_menu(request):
    return render(request, 'menu.html')

def leave_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.date = datetime.date.today()
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'review.html', context)
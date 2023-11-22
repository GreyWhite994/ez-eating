from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation, Review
from .forms import ReservationForm, ReviewForm 
import datetime


@login_required
def get_booking_list(request):
    """get_booking_list function

    takes all objects from Reservation

    returns booking_list.html with context
    """
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'booking_list.html', context)


def create_reservation(request):
    """create_reservation function

    takes reservation form and if is valid returns updated booking list

    else resets and returns create_reservation.html with context
    """
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
    """ edit_reservation function

    takes reservation object based on reservation_id and if form is valid
    updates accordingly and returns booking_list.html

    else returns edit_reservation.html with context
    """
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
    """ delete_reservation function

    gets reservation based on reservation_id and deletes reservation

    returns get_booking_list
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
    return redirect('get_booking_list')

def get_home(request):
    """ get_home function

    takes all objects from Review

    returns index.html with context
    """
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'index.html', context)

def get_menu(request):
    """ get_menu function

    returns menu.html
    """
    return render(request, 'menu.html')

def leave_review(request):
    """ leave_review function

    takes ReviewForm and if valid form is saved and
    date field is populated with current date and returned to home

    else returned to review.html
    """
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
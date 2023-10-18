from django.shortcuts import render

# Create your views here.


def get_booking_list(request):
    return render(request, 'booking/booking_list.html')

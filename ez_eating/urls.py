"""ez_eating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking', views.get_booking_list, name='get_booking_list'),
    path('create', views.create_reservation, name='create_reservation'),
    path('edit/<reservation_id>', views.edit_reservation, name='edit'),
    path('delete/<reservation_id>', views.delete_reservation, name='delete'),
    path("accounts/", include("allauth.urls")),
    path('', views.get_home, name='home'),
    path('menu', views.get_menu, name='menu'),
    path('review', views.leave_review, name='review'),
]

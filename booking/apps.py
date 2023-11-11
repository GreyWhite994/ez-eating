from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'review'
# Generated by Django 3.2.22 on 2023-11-05 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_reservation_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together={('date', 'time')},
        ),
    ]

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Room(models.Model):
    number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        unique=True
    )
    capacity = models.PositiveIntegerField(
        validators=MinValueValidator(1)
    )
    price_for_night = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return "Room - {}".format(self.number)


class Reservation(models.Model):
    room = models.ForeignKey(
        'reservations.Room'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return "Reservation {} {}".format(
            self.user.first_name,
            self.user.last_name
        )

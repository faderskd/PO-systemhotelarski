import datetime

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.core.validators import MinValueValidator


class Room(models.Model):
    number = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        unique=True
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    price_for_night = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return "Room - {}".format(self.number)


class ReservationManager(models.Manager):
    def active(self):
        now = datetime.datetime.now()
        return self.get_queryset().filter(end_date__gte=now)

    def inactive(self):
        now = datetime.datetime.now()
        return self.get_queryset().filter(end_date__lt=now)

    def user_active(self, user_pk):
        return self.active().filter(user__pk=user_pk)

    def user_inactive(self, user_pk):
        return self.inactive().filter(user__pk=user_pk)


class Reservation(models.Model):
    room = models.ForeignKey(
        'reservations.Room'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    objects = ReservationManager()

    class Meta:
        ordering = ('start_date', )

    def __str__(self):
        return "Reservation {} {}".format(
            self.user.first_name,
            self.user.last_name
        )

    @classmethod
    def reservation_exists(cls, start_date, end_date, room):
        reservation_exists = cls.objects.filter(
            (Q(end_date__lte=end_date) & Q(end_date__gt=start_date)) |
            (Q(start_date__lt=end_date) & Q(start_date__gte=start_date)) |
            (Q(start_date__lte=start_date) & Q(end_date__gte=end_date)),
            room=room
        ).exists()
        return reservation_exists

    @property
    def is_active(self):
        now = datetime.datetime.now()
        return self.end_date >= now




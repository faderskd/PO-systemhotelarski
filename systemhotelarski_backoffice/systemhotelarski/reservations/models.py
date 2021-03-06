import datetime

from django.db import models
from django.db.models import Q
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
    def find_room(self, start_date, end_date, capacity, exclude):
        reservations_from_dates = self.get_queryset().filter(
            (Q(end_date__lte=end_date) & Q(end_date__gt=start_date)) |
            (Q(start_date__lt=end_date) & Q(start_date__gte=start_date)) |
            (Q(start_date__lte=start_date) & Q(end_date__gte=end_date)),
        )

        if exclude:
            reservations_from_dates = reservations_from_dates.exclude(
                id=exclude.id
            )

        reserved_rooms = reservations_from_dates.values_list(
            'room',
            flat=True
        )

        rooms = Room.objects.filter(capacity=capacity).exclude(id__in=reserved_rooms)
        return rooms.first()

    def active(self):
        now = datetime.datetime.now().date()
        return self.get_queryset().filter(end_date__gte=now)

    def inactive(self):
        now = datetime.datetime.now().date()
        return self.get_queryset().filter(end_date__lt=now)

    def user_active(self, user_pk):
        return self.active().filter(user_pk=user_pk)

    def user_inactive(self, user_pk):
        return self.inactive().filter(user_pk=user_pk)


class Reservation(models.Model):
    room = models.ForeignKey(
        'reservations.Room'
    )
    user_pk = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

    objects = ReservationManager()

    class Meta:
        ordering = ('start_date', )

    def __str__(self):
        return "Reservation {}".format(
            self.user_pk
        )

    @property
    def capacity(self):
        return self.room.capacity




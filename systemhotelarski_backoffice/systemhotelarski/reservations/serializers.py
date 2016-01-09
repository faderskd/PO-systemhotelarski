from django.core.validators import ValidationError

from rest_framework import serializers

from .models import Reservation, Room


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('id', 'room', 'user', 'start_date', 'end_date', )

    def _dates_are_valid(self, start_date, end_date):
        delta = end_date - start_date
        print(delta.days)
        if delta.days < 1:
            raise ValidationError('Incorrect dates')
        return True

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        room = data.get('room')

        if not self._dates_are_valid(start_date, end_date):
            raise ValidationError('Incorrect dates')

        if Reservation.reservation_exists(start_date, end_date, room):
            raise ValidationError('This room is reserved in this period')

        return data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'number', 'capacity', 'price_for_night',)

